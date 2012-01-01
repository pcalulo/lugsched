
var Gui = {};
var Core = {};
var Network = {};

Gui.showRegistrationPanel = function() {
	$("#otherUniversityMessage").slideDown();
	$("#searchWidgets").slideUp();
}

Gui.showSearchPanel = function() {
	$("#otherUniversityMessage").slideUp();
	$("#searchWidgets").slideDown();
}

Gui.onUniversitySelected = function() {
	var uni = $("#universityBox").val();
	if (uni == "other") {
		$("#otherUniversityMessage").slideDown(200);
	} else {
		$("#otherUniversityMessage").slideUp(200);
	}
}

Gui.areUniDetailsEntered = function() {
	var name = $("#uniNameTextBox").val();
	var termCount = $("#termCountBox").val();
	
	if (name && (termCount != "?")) {
		return true;
	}
	return false;
}

Gui.isCourseLengthInputValid = function() {
	var entered = $("#courseLengthBox").val();
	return !(isNaN(entered) || isNaN(parseInt(entered)))
}

Gui.checkInputValidity = function() {
	// isNaN alone does not catch ""
	if (!Gui.isCourseLengthInputValid()) {
		$("#enteredLengthIsNaNMessage").slideDown(200);
		return false;
	} else {
		$("#enteredLengthIsNaNMessage").slideUp(200);
		return true;
	}
}

Gui.isDataComplete = function() {
	if (UniSearch.hasSelectedUni()) {
		return true;
	} else if (Gui.isCourseLengthInputValid() && Gui.areUniDetailsEntered()) {
		return true;
	}
	return false;
}

Core.createJson = function() {
	data = new Object();
	data.selectedUni = UniSearch.selectedUni;

	data.uniTextBox = $("#uniNameTextBox").val();
	data.termCount = $("#termCountBox").val();
	data.courseLength = $("#courseLengthBox").val();
	data.shouldAutofillEndTime = $("#shouldAutofillBox").is(":checked");
	
	return JSON.stringify(data);
}

Network.updateJson = function() {
	$("input[name=profileData]").val(Core.createJson());
}


Network.sendProfileData = function() {
	if (Gui.isDataComplete()) {
		$("#fillInEverythingMessage").slideUp(200);
		Network.updateJson();
		$("#profileDataForm").submit();
		console.log("Complete!");
	} else {
		console.log("Incomplete!");
		$("#fillInEverythingMessage").slideDown(200);
	}
}

Network.sendUniSearchQuery = function(query) {
	data = new Object();
	data.action = "university_search";
	data.arg0 = query;
	$.getJSON("/rpc/search", data, UniSearch.onDataReceived);
}

Network.getAllUniversities = function(query) {
	data = new Object();
	data.action = "university_getall";
	$.getJSON("/rpc/search", data, UniSearch.onDataReceived);
}


$(document).ready(function() {
	$("#universityBox").change(Gui.onUniversitySelected);
	$("#courseLengthBox").blur(Gui.checkInputValidity)
	UniSearch.initialize();
});
