
function University() {
	this.name = "Default University"
	this.address = "-1 Undefined Avenue"
	this.termsPerYear = 2
}

function Schedule() {
	this.term = 1
	this.year = 2011
	this.classes = []
}

function dummyDataCallback(data, status, jqXHR) {
	if (status == "success") {
		console.log("Request successful.");
	} else {
		console.error("Encountered server-side error ("
			+ status + ")");
	}
}

function sendDummyData() {
	data = new Object()

	uni = new University()
	uni.name = "De La Salle University"
	uni.address = "2401 Taft Avenue, Malate, Manila"
	uni.termsPerYear = 3
	
	data.json = JSON.stringify(uni)
	$.post('/api/university', data, dummyDataCallback);
	/*
	data = new Object()
	data.entityKey = 'ag1mb3JldmVyLWFsb25lchALEgpVbml2ZXJzaXR5GAIM'
	$.getJSON('/api/university', data, function(data, status, jqXHR) {
		console.log(data)
	});
	//*/
}

function sendDummySchedule() {
	data = new Object()
	data.json = JSON.stringify(new Schedule())
	$.post('/api/schedule', data, dummyDataCallback)
}

function sendDummyCourse() {
	data = new Object()
	course = new Object()
	course.courseCode = "HCIFACE"
	course.description = "Make easy to use, shiny stuff"
	$.getJSON("/api/university", null, function(received, status, jqXHR) {
		if (received.length == 0) {
			console.debug("No universities found - add some first");
			return
		}
		course.universityKey = received[0].entityKey
		data.json = JSON.stringify(course)
		$.post("/api/course", data, dummyDataCallback)
	})
}

function sendDummySection() {
	var data = {}
	var section = {}

	var courses;
	// Grab some courses
	$.getJSON("/api/course", null, function(received, status, jqXHR) {
		courses = received
		console.debug(courses)
		if (courses.length == 0) {
			console.debug("No courses found - add some first")
			return
		}
		section.name = "S22"
		section.days = "MH"
		section.courseKey = courses[0].entityKey
		data.json = JSON.stringify(section)
		$.post('/api/section', data, dummyDataCallback)
	});
}

function sendDummyProfile() {
	var data = new Object()
	var profile = new Object()
	
}

function updateSchedule() {
	var data = new Object();
	
}


function setCurrentSchedule() {
	$.getJSON("/api/schedule", null, function(schedules, status, jqXHR) {
		if (schedules.length == 0) {
			console.debug("No schedules found - add some first")
			return
		}
		var data = new Object()
		data.entityKey = schedules[0].entityKey
		$.post('/api/schedule/current', data, dummyDataCallback)
	});
}

function unsetCurrentSchedule() {
	$.post("/api/schedule/current", null, function() {
		console.log("Current schedule has been unset");
	});
}

function getFirstSection(callback) {
	$.getJSON("/api/section");
}

Meeting = {}
Meeting.MON = 0x01
Meeting.TUE = 0x02
Meeting.WED = 0x04
Meeting.THU = 0x08
Meeting.FRI = 0x10
Meeting.SAT = 0x20


function makeTime(hour, minute) {
	var time = {}
	time.hour = hour;
	time.minute = minute;
	return time;
}

function sendDummyMeeting(section) {
	var data = new Object();
	var meeting = new Object();
	
	$.getJSON("/api/section", null, function(received, status, jqXHR) {
		if (received.length == 0) {
			console.debug("No sections found - add some first");
			return
		}
		meeting.sectionKey = received[0].entityKey
		meeting.days = Meeting.MON | Meeting.THU
		meeting.isSpecificDay = false
		meeting.startTime = makeTime(9, 40);
		meeting.endTime = makeTime(11, 10);
		data.json = JSON.stringify(meeting)
		$.post("/api/meeting", data, dummyDataCallback);
	})
}

function createDefaultProfile() {
	$.post("/api/profile", null, dummyDataCallback)
}

function deleteProfile() {
	$.ajax({
		url: "/api/profile",
		type: "DELETE",
		success: dummyDataCallback
	});
}

function setUniversity() {
	$.getJSON("/api/university", null, function(unis, status, jqXHR) {
		if (unis.length == 0) {
			console.log("No universities found - add some first");
			return;
		}
		$.getJSON("/api/profile", null, function(profile, status, jqXHR) {
			profile.universityKey = unis[0].entityKey;
			var data = {}
			data.json = JSON.stringify(profile)
			$.post("/api/profile", data, dummyDataCallback);
		});
	});
}

function createEnrollment() {
	var data = {}
	enrollment = {}
	$.getJSON("/api/schedule/current", null, function(schedule, status, jqXHR) {
		if (!schedule) {
			console.log("No current schedule!")
			return
		}
		console.log("Got schedule " + schedule.entityKey)
		$.getJSON("/api/section", null, function(sections, status, jqXHR) {
			if (sections.length == 0) {
				console.log("Add some sections first!")
				return
			}
			console.log("Got section " + sections[0].entityKey)
			enrollment.scheduleKey = schedule.entityKey
			enrollment.sectionKey = sections[0].entityKey
			data.json = JSON.stringify(enrollment)
			$.post("/api/enrollment", data, dummyDataCallback)
		});
	});
}

function createFullSchedule() {
	var data = {}
	var schedule = {}
	schedule.year = 2011
	schedule.term = 1
	schedule.entityKey = ''
	schedule.classes = []
	
	$.getJSON("/api/section", null, function(sections, status, jqXHR) {
			if (sections.length == 0) {
				console.log("Add some sections first!")
				return
			}
			console.log("Got section " + sections[0].name + " - " + sections[0].entityKey)
			var section = sections[0]
			schedule.classes.push(section)
			data.json = JSON.stringify(schedule)
			console.log(data.json);
			
			$.post("/api/schedule", data, dummyDataCallback);
		});
}

