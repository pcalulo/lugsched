var gui = {};

gui.curSched = {}
gui.curSched.init = function() {
	this.clist = new ClickList($("#currentScheduleList"));
	schedules.getUserScheduleData(this.onScheduleDataReceived);
}

gui.curSched.onScheduleDataReceived = function(data, status, jqXHR) {
	if (data.courses) {
		if (data.courses.length == 0) {
			gui.curSched.clist.setEmptyText("Your current schedule is empty");
			return;
		}
		$.each(data.courses, function(index, course) {
			var elem = new ClickListElement();
			elem.mainText = course.courseCode + " " + course.section;
			elem.subText = course.days + " " + TimeUtils.formatTimeRange(course.startTime, course.endTime);
			gui.curSched.clist.add(elem);
		});
	} else {
		gui.curSched.clist.setEmptyText("You do not have a current schedule");
	}
}

gui.registerItemAnimations = function() {
	$("#userSchedulesList > div.listItem").hover(function() {
		$(this).addClass("scheduleList-hover");
		$(".scheduleList-hover > div.button-bag").show();
	}, function() {
		$(".scheduleList-hover > div.button-bag").hide();
		$(this).removeClass("scheduleList-hover");
	})
	
	$("#userSchedulesList > div.listItem").removeClass("listItem-bottom");
	$("#userSchedulesList > div.listItem:last").addClass("listItem-bottom");
}

gui.utils = {}
gui.utils.setAttrs = function(widget, schedule) {
	widget.attr("scheduleName", schedule.name);
	widget.attr("scheduleKey", schedule.key);
}

gui.utils.addButtons = function(widget) {
	$("#userSchedulesList > div.listItem:last").append("<div class='button-bag'></div>");
	var buttonBag = $("#userSchedulesList > div.listItem:last > div.button-bag");
	buttonBag.append(
		"<input type='button' value='Edit'></input>")
	buttonBag.append(
		"<input type='button' value='Delete'></input>")
	buttonBag.append(
		"<input type='button' value='Share'></input>")
	return buttonBag;
}

gui.utils.initEditButton = function(buttonBag, schedule) {
	gui.utils.setAttrs(buttonBag.find("input[value=Edit]"), schedule);
	buttonBag.find("input[value=Edit]").click(function() {
		var scheduleName = $(this).attr("scheduleName");
		$("#editScheduleForm > input[name=key]").val($(this).attr("scheduleKey"));
		$("#editScheduleForm").submit();
	})
}

gui.utils.initDeleteButton = function(buttonBag, schedule) {
	gui.utils.setAttrs(buttonBag.find("input[value=Delete]"), schedule);
	buttonBag.find("input[value=Delete]").click(function() {
		var scheduleName = $(this).attr("scheduleName");
		apprise("Are you sure you want to delete \"" + scheduleName +"\"?",
			{'verify':true}, function(input) {
				if (input) {
					schedules.deleteByKey(schedule.key);
				}
			});
	})
}

gui.utils.initShareButton = function(buttonBag, schedule) {
	gui.utils.setAttrs(buttonBag.find("input[value=Share]"), schedule);
	buttonBag.find("input[value=Share]").click(function() {
		var scheduleName = $(this).attr("scheduleName");
		gui.showSharePrompt(scheduleName)
	})
}

gui.utils.createSubtext = function(schedule) {
	var courseNoun = (schedule.courseCount == 1) ? "course" : "courses";
	return schedule.courseCount + ' ' + courseNoun + ', AY ' + schedule.year + '-' + (+schedule.year + 1) +
		' Term ' + schedule.term;
}

/* 
 * TODO: Messy, fix NAO!
 * Use ClickList for the schedules list 
 */
gui.add = function(schedule) {
	var buttonBag;
	var schedList = $("#userSchedulesList");
	// Remove the no schedules message
	schedList.find("p").remove();
	
	// Add the schedule to the list
	schedList.append('<div class="listItem"><b>' + schedule.name + '</b>' +
		'<br><div class="smallText">' + gui.utils.createSubtext(schedule) +'</div></div>');
	
	gui.utils.setAttrs($("#userSchedulesList > div.listItem:last"), schedule);
	buttonBag = gui.utils.addButtons();
	
	gui.utils.initEditButton(buttonBag, schedule);
	gui.utils.initDeleteButton(buttonBag, schedule);
	gui.utils.initShareButton(buttonBag, schedule); 
	
	gui.registerItemAnimations();
	
	// Return the newly created list item, so we can apply some artsy-fartsy if we want to.
	return $("#userSchedulesList > div.listItem:last");
}

gui.showSharePrompt = function(scheduleName) {
	var email;
	apprise("Enter the Google Account of the person you want to share \"" + scheduleName +
		"\" to. (Don't worry, no emails will be sent)", {'input': true}, function(r) {
		email = r;
		if (email == "" || email == " ") return;
		if (!email) return;
		schedules.share(scheduleName, email);
	});
}


gui.shared = {};
gui.shared.init = function() {
	var elem;
	var clist = gui.shared.clist = new ClickList($("#sharedSchedulesCList"));
	
	for (i = 0; i < sharedScheds.length; i++) {
		gui.addShared(sharedScheds[i]);
	}
}

gui.addShared = function(schedule) {
	var elem = new ClickListElement();
	elem.mainText = schedule.name;
	elem.subText = "From <b>" + schedule.owner + "</b>, ";
	elem.subText += gui.utils.createSubtext(schedule);
	elem.button1.text = "View";
	elem.button1.onClick = function() {
		var form = $("#viewSharedScheduleForm");
		form.find("input[name=shareKey]").val(schedule.shareKey);
		form.submit();
	}
	
	
	var widget = gui.shared.clist.add(elem);
}

gui.callbacks = {};
gui.callbacks.createSchedule = function() {
	enteredName = $("input[name=scheduleNameBox]").val();
	console.log(enteredName);	
	if (enteredName == "") {
		$("#unnamedScheduleMessage").slideDown(200).delay(5000).slideUp(200);
		return;
	}
	$("#unnamedScheduleMessage").slideUp(200);
	$("input[name=scheduleNameBox]").hide();
	$("#createScheduleSpinner").show();
	$("input[name=scheduleNameBox]").val("");
	$("input[name=scheduleNameBox]").blur();
	schedules.sendCreationRequest(enteredName);
}

gui.callbacks.onCreationRequestComplete = function(json, status, jqXHR) {
	var item;
	var data = $.parseJSON(json);
	$("#createScheduleSpinner").hide();
	$("input[name=scheduleNameBox]").show();
	$("input[name=showCreateScheduleWidgetsButton]").show();
	if (data.success) {
		item = gui.add(data.schedule);
		console.log(json);
		item.hide();
		item.slideDown(200);
		userScheds.push(data.schedule.name);
	} else {
		if (data.reason == "non-unique") {
			$("#duplicateScheduleMessage").slideDown(200);
		} else {
			console.log("Failed with no provided reason");
		}
	}
}

gui.callbacks.scheduleInputBox = {};
gui.callbacks.scheduleInputBox.idleText = "Create a new schedule";

gui.callbacks.scheduleInputBox.focusGained = function() {
	if ($(this).val() == gui.callbacks.scheduleInputBox.idleText) {
		$(this).val("");
		$(this).removeClass("faded-out");
	}
}

gui.callbacks.scheduleInputBox.focusLost = function() {
	if ($(this).val() == "") {
		$(this).val(gui.callbacks.scheduleInputBox.idleText);
		$(this).addClass("faded-out");
	}
}

gui.callbacks.scheduleInputBox.init = function() {
	$("#scheduleNameBox").focus(gui.callbacks.scheduleInputBox.focusGained);
	$("#scheduleNameBox").blur(gui.callbacks.scheduleInputBox.focusLost);
	$("#scheduleNameBox").blur();

	// Pressing enter while the schedule name box is in focus should create the schedule.
	$("input[name=scheduleNameBox]").keydown(function(event) {
		if (event.which == 13) {
			gui.callbacks.createSchedule();
		}
	})

}


// Sharing
gui.callbacks.onShareRequestComplete = function(json, status, jqXHR) {
	console.log(json)
	data = JSON.parse(json)
	if (data.success) {
		$("#scheduleSharedMessage").slideDown(200).delay(5000).slideUp(200);
	} else {
		$("#shareFailedMessage > span").text(data.reason);
		$("#shareFailedMessage").slideDown(200);
	}
}
