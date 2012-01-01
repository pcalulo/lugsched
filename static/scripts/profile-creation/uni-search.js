
UniSearch = {}

UniSearch.initSearchBox = function() {
	var idleText = "Your school's name begins with...";
	var searchBox = $("#uniSearchBox");
	searchBox.focus(function() {
		if ($(this).val() == idleText) {
			$(this).val("");
			$(this).removeClass("faded-out");
		}
	});
	searchBox.blur(function() {
		if ($(this).val() == "") {
			$(this).val(idleText);
			$(this).addClass("faded-out");
		}
	});
	searchBox.keydown(function(event) {
		if (event.which == 13) {
			UniSearch.onSearchPressed();
		}
	})
	searchBox.blur();
}

UniSearch.onSearchPressed = function() {
	Network.sendUniSearchQuery($("#uniSearchBox").val());
}

UniSearch.getAll = function() {
	Network.getAllUniversities();
}

UniSearch.hasSelectedUni = function() {
	return !!UniSearch.selectedUni;
}

UniSearch.selectUniversity = function(university) {
	$("#universityNameLabel").text(university.name);
	$("#universitySelectedMessage").slideDown();
	$("input[name=uniKey]").val(university.key);

	$("#otherUniversityMessage").slideUp();
	$("#searchWidgets").slideUp();
	UniSearch.selectedUni = university;
}

UniSearch.clearSelection = function() {
	$("#universitySelectedMessage").slideUp();
	$("input[name=uniKey]").val("");

	$("#otherUniversityMessage").slideUp();
	$("#searchWidgets").slideDown();
}


UniSearch.onDataReceived = function(data, status, jqXHR) {
	var elem;
	var clist = UniSearch.clist;
	clist.removeAll();
	for (i = 0; i < data.length; i++) {
		var university = data[i]
		elem = new ClickListElement();
		elem.mainText = university.name;
		elem.subText = university.key;
		elem.button1.text = "Select";
		elem.button1.onClick = function() {
			UniSearch.selectUniversity(university);
		}
		clist.add(elem);
	}
	$("#addUniTip").slideDown();
}

UniSearch.initialize = function() {
	UniSearch.clist = new ClickList($("#universityList"));
	UniSearch.initSearchBox();
	console.log("HERRO");
}



