
var Network = {}

var clist;
Network.onReceive = function(data, status, jqXHR) {
	console.log("HERRO!")
	var elem;
	for (i = 0; i < data.length; i++) {
		var course = data[i]
		elem = new ClickListElement();
		elem.mainText = course.courseCode + " " + course.section;
		elem.subText = course.room + " " + course.days;
		clist.add(elem)
	}
}

$(document).ready(function() {
	clist = new ClickList($("#mergeList"));
	var sd = new ScheduleDisplay($("#schedDisp"));

	var otherList = new ClickList($("#sharedSchedulesList"));

	for (i = 0; i < 5; i++) {
		var elem = new ClickListElement();
		elem.mainText = "Herp Derp longtext ekrjwkejaegkjergkejrghkehgkjer " + i;
		elem.subText = "herp@derp.lol";
		otherList.add(elem);
	}

	var data = new Object();
	data.action = "get_shared_schedule";
	data.arg0 = setting_sharekey;
	$.getJSON('/rpc/search', data, Network.onReceive)
});

