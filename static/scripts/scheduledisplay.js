
function ScheduleDisplay(div) {
	this.div = div;
	this.initializeDiv(div);
}

ScheduleDisplay.prototype.days = [
	"monday", "tuesday", "wednesday",
	"thursday", "friday", "saturday"
]

ScheduleDisplay.prototype.createDayDivHTML = function(day) {
	var html = "<div class='scheduledisplay-" + day + "'>";
	html += "<div class='scheduledisplay-day-header'></div>"
	html += "<div class='scheduledisplay-clist'></div>";
	html += "</div>"
	return html;
}

ScheduleDisplay.prototype.initializeDiv = function(div) {
	// Keep the ScheduleDisplay reachable inside the following
	// anonymous function
	var sdisp = this;
	this.clists = new Object();

	$.each(this.days, function(index, day) {
		div.append(sdisp.createDayDivHTML(day));
		var clistDiv = div.find("scheduledisplay-clist:last");
		sdisp.clists[day] = new ClickList(clistDiv);
	})
	
	div.find("div").hide();
}

ScheduleDisplay.prototype.addSchedule = function(schedule) {
	var courses = schedule.courses;
	
}

