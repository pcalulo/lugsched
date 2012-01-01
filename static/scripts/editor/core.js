
var courseCount = 0;
var MAXIMUM_COURSE_COUNT = 14;
var courses = new Array();
var schedData = new Object();

var Courses = {};
var Utils = {};
var Network = {};

function Course() {	
}

Courses.canAddCourse = function() {
	return courseCount < MAXIMUM_COURSE_COUNT;
}

Courses.add = function(courseCode, section, room, startTime, endTime, days) {
	if (!Courses.canAddCourse()) {
		return;
	}
	var newCourse = new Course();
	newCourse.courseCode = courseCode;
	newCourse.section = section;
	newCourse.room = room;
	newCourse.days = days;
	
	var parsedStart = Utils.parseTime(startTime);
	var parsedEnd = Utils.parseTime(endTime);
	
	if (parsedStart && parsedEnd) {
		newCourse.startTime = parsedStart;
		newCourse.endTime = parsedEnd;
	} else {
		console.log("Unable to parse time");
		return 0;
	}
	
	courses.push(newCourse);
	Network.updateJson();
	
	return newCourse;
}

Courses.remove = function(courseCode) {
	for (i = 0; i < courses.length; i++) {
		if (courses[i].courseCode == courseCode) {
			courses.splice(i, 1);
			break;
		}
	}
	Network.updateJson();
}


Utils.parseTime = function(rawTime) {
	time = new Object();
	
	time.hour = Math.floor(rawTime / 100);
	time.minute = rawTime % 100;
	
	if (time.hour > 0 && time.minute >= 0) {
		return time;
	}
	
	// Prepending a date forces time entered as "0800" to be interpreted as 8am
	dTime = Date.parse("1/1/1970 " + rawTime);
	if (dTime) {
		time.hour = dTime.getHours();
		time.minute = dTime.getMinutes();
		return time;
	}
	
	return false;
}

Network.updateJson = function() {
	schedData.newSchedName = $("input[name=newSchedName]").val();
	schedData.courses = courses;
	schedData.isCurrent = $("#isCurrentCheckbox").is(":checked");
	schedData.term = $("#termBox").val();
	schedData.year = $("#yearBox").val();
	$("input[name=scheduleJSON]").val(JSON.stringify(schedData));
}

Network.onCoursesReceived = function(data, success, jqXHR) {
	var i;
	var course;
	for (i = 0; i < data.length; i++) {
		course = data[i];
		console.log(course.courseCode);
		Gui.addCourse(course);
		courses.push(data[i]);
	}
	$("#loadingMessage").hide();
	Network.updateJson();
}

Network.getCourses = function() {
	var args = new Object();
	args.action = "get_courses";
	args.arg0 = $("input[name=scheduleKey]").val();
	
	$.getJSON('/rpc/search', args, Network.onCoursesReceived)
}

