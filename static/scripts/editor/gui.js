
var Gui = {};

Gui.addCourse = function(course) {
	var elem = new ClickListElement();
	elem.mainText = course.courseCode + " (" + course.section + ")";
	elem.subText = CourseUtils.createSubText(course);

	elem.button1.text = "Delete";
	elem.button1.onClick = function() {
		Courses.remove(course.courseCode);
		clist.remove(elem);
		clist.fullUpdate();
	}

	elem.button2.text = "Edit";
	elem.button2.onClick = function() {
		Gui.editCourseData(course);
		Courses.remove(course.courseCode);
		clist.remove(elem);
		clist.fullUpdate();
	}

	clist.add(elem);
}


Gui.isCourseDataComplete = function() {
	var courseCode = $("input[name=newCourseCode]").val() 
	var section = $("input[name=newSection]").val()
	var room = $("input[name=newRoom]").val()
	var startTime = $("input[name=newStartTime]").val()
	var endTime = $("input[name=newEndTime]").val()
	var days = $("input[name=newDays]").val()
	
	if (courseCode == "Course code") return 0;
	if (section == "Section") return 0;
	if (room == "Room") return 0;
	if (startTime == "Start time") return 0;
	if (endTime == "End time") return 0;
	if (days == "Days") return 0;
	
	return 1;
}


Gui.handlers = {};
Gui.handlers.addEnteredCourse = function() {
	var courseCode = $("input[name=newCourseCode]").val()
	var section = $("input[name=newSection]").val()
	var room = $("input[name=newRoom]").val()
	var startTime = $("input[name=newStartTime]").val()
	var endTime = $("input[name=newEndTime]").val()
	var days = $("input[name=newDays]").val()
	
	if (!Gui.isCourseDataComplete()) {
		alert("Please fill in all the fields.");
		return;
	}
	
	var course = Courses.add(courseCode, section, room, startTime, endTime, days);
	if (course) {
		Gui.addCourse(course);
		clearCourseInputs();
	} else {
		alert("I couldn't figure out the time you entered. Please check it.");
	}
}

Gui.editCourseData = function(courseData) {
	$("input[name=newCourseCode]").val(courseData.courseCode).removeClass("faded-out");
	$("input[name=newSection]").val(courseData.section).removeClass("faded-out");
	$("input[name=newRoom]").val(courseData.room).removeClass("faded-out");
	$("input[name=newStartTime]").val(TimeUtils.formatTime(courseData.startTime)).removeClass("faded-out");
	$("input[name=newEndTime]").val(TimeUtils.formatTime(courseData.endTime)).removeClass("faded-out");
	$("input[name=newDays]").val(courseData.days).removeClass("faded-out");
}

function clearCourseInputs() {
	$("input[name=newCourseCode]").val("Course code").addClass("faded-out");
	$("input[name=newSection]").val("Section").addClass("faded-out");
	$("input[name=newRoom]").val("Room").addClass("faded-out");
	$("input[name=newStartTime]").val("Start time").addClass("faded-out");
	$("input[name=newEndTime]").val("End time").addClass("faded-out");
	$("input[name=newDays]").val("Days").addClass("faded-out");
	$(".searchResultsBox").slideUp(200);
}

function showNoCoursesMessage() {
	$("#no-courses-text").show();
}

function genericBoxBlurHandler(boxName, defaultText) {
	var box = $("input[name=" + boxName +"]");
	if (box.val() == "") {
		box.val(defaultText);
		box.addClass("faded-out");
	}
}

function genericBoxFocusHandler(boxName, defaultText) {
	var box = $("input[name=" + boxName +"]");
	if (box.val() == defaultText) {
		box.val("");
		box.removeClass("faded-out")
	}
}

function addBoxFocusHandlers(boxName, defaultText) {
	var box = $("input[name=" + boxName + "]")
	box.val(defaultText);
	box.addClass("faded-out")
	box.focus(function() {
		genericBoxFocusHandler(boxName, defaultText);
	});
	box.blur(function() {
		genericBoxBlurHandler(boxName, defaultText);
	});
}

function courseSorter(courseA, courseB) {
	return courseA.courseCode > courseB.courseCode;
}


var clist;

$(document).ready(function() {
	$("#no-courses-text").hide();
	$("#updatingMessage").hide();
	
	addBoxFocusHandlers("newCourseCode", "Course code");
	addBoxFocusHandlers("newSection", "Section");
	addBoxFocusHandlers("newRoom", "Room");
	addBoxFocusHandlers("newStartTime", "Start time");
	addBoxFocusHandlers("newEndTime", "End time");
	addBoxFocusHandlers("newDays", "Days");
	
	$("input[name=newCourseCode]").blur(function() {
		if ($("input[name=newCourseCode]").val() != "" && $("input[name=newCourseCode]").val() != "Course code") {
			Sections.getFor($("input[name=newCourseCode]").val());
		}
		genericBoxBlurHandler("newCourseCode", "Course code");
	});

	clist = new ClickList($("#test-list"));
	
	$("input[name=newSchedName]").blur(function() {
		Network.updateJson();
	})
	
	// The setting_* variables are initialized within a <script> tag in the HTML
	$("#yearBox").change(Network.updateJson);
	$("#yearBox").val(setting_year);
	$("#termBox").change(Network.updateJson);
	$("#termBox").val(setting_term);
	
	$(".searchResultsBox").hide();

	if (setting_isCurrentSchedule) {
		$("#isCurrentCheckbox").attr("checked", "checked");
	}
	
	Network.getCourses();
	$("#course-table").hide();
	registerMenuItemAnimations();
	Network.updateJson();
});


function registerMenuItemAnimations() {
	$(".menuItem").hover(function() {
		$(this).addClass("menuItem-hover");
	}, function() {
		$(".menuItem").removeClass("menuItem-hover");
	});
}

function registerCourseListAnimations() {
	$('#course-table tbody > tr:not(:first)').hover(function() {
		$(this).addClass("tableItem-hover");
		$('.tableItem-hover > td > input').show()
	}, function() {
		$('.tableItem-hover > td > input').hide()
		$(this).removeClass("tableItem-hover");
	})
}

function toggleSearchBox() {
	$(".searchResultsBox").slideToggle(200);
}
