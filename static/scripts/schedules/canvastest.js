
function canvas_main() {
    var schedDisp = new ScheduleDisplay(document.getElementById("chart-canvas"));
    schedDisp.addCourse(new Course());
}

$(document).ready(canvas_main);

