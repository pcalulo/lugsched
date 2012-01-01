
var Sections = {};
Sections.callbacks = {};
Sections.callbacks.onReceive = function(data, status, jqXHR) {
	var knownSections = [];
	$("#searchResults > div").remove();
	$("#searchResults").html("Known sections: ");
	
	for (i = 0; i < data.length; i++) {
		course = data[i];
		knownSections.push(course);
		$("#searchResults").append(
			"<div class=\"menuItem\"><b>" +
			course.section + "</b> (" + course.room + ", " +
			Utils.formatTimeRange(course.startTime, course.endTime) + 
			", " + course.days + ")</div>"
		)
		
		// 
		$("#searchResults > div:last").attr("resultIndex", i)
		$("#searchResults > div:last").click(function() {
			index = $(this).attr("resultIndex");
			courseData = knownSections[index];
			Gui.editCourseData(courseData);
		});
	}
	
	if (data.length > 0)
		$(".searchResultsBox").slideDown(200);
	else
		$(".searchResultsBox").slideUp(200);
	registerMenuItemAnimations();
}

Sections.getFor = function(courseCode) {
	var args = new Object();
	args.action = "course_search";
	args.arg0 = courseCode;
	
	if (courseCode != "Course code" && courseCode != "") {
		$.getJSON('/rpc/search', args, Sections.callbacks.onReceive);
	} else {
		$(".searchResultsBox").slideUp(200)
	}
}
