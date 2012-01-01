
console.log("TimeUtils loading");

TimeUtils = {};

TimeUtils.formatTime = function(time) {
	var formatted = "";
	var hour = time.hour;
	var minute = time.minute;
	
	if (hour > 12)
		hour -= 12;
	
	if (minute < 10)
		minute = "0" + minute;
	
	formatted = hour + ":" + minute;
	
	if (time.hour >= 12)
		formatted += "pm"
	else
		formatted += "am";
	
	return formatted;
}

TimeUtils.formatTimeRange = function(startTime, endTime) {
	return TimeUtils.formatTime(startTime) + " - " + TimeUtils.formatTime(endTime);
}

CourseUtils = {}
CourseUtils.createSubText = function(course) {
	return  course.days + " " +
		course.room + " " +
		TimeUtils.formatTimeRange(course.startTime, course.endTime);
}

