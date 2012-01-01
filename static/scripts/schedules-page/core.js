$(document).ready(function() {
	for (i = 0; i < userScheds.length; i++) {
		gui.add(userScheds[i]);
	}
	gui.registerItemAnimations();
	gui.curSched.init();
	gui.callbacks.scheduleInputBox.init();
	
	// If the user doesn't have any schedules
	if (userScheds.length == 0) {
		$("#userSchedulesList").append("<p>You haven't created any schedules yet.</p>");
	}
	
	gui.shared.init();
});

var schedules = {};

schedules.getUserScheduleData = function(callback) {
	data = new Object();
	data.action = "get_current_schedule"
	$.getJSON("/rpc/search", data, callback);
}

schedules.deleteByKey = function(key, callback) {
	$("#deleteScheduleForm > input[name=key]").val(key);
	$("#deleteScheduleForm").submit();
}

schedules.sendCreationRequest = function(scheduleName) {
	data = new Object();
	data.scheduleName = scheduleName;
	$.post("/rpc/create-schedule", data, gui.callbacks.onCreationRequestComplete);
}



// Sharing
schedules.share = function(scheduleName, shareToEmail) {
	data = new Object();
	data.scheduleName = scheduleName;
	data.shareToEmail = shareToEmail;
	$.post("/rpc/share-schedule", data, gui.callbacks.onShareRequestComplete)
}
