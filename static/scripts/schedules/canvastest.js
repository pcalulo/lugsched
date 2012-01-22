
function canvas_main() {
    var schedDisp = new ScheduleDisplay(document.getElementById("chart-canvas"));
    schedDisp.addCourse(new Course());

    var course = new Course();
    course.code = 'HIWRLD';
    course.section.meetings[0].startTime.setHours(13);
    course.section.meetings[0].endTime.setHours(14);
    schedDisp.addCourse(course)

    schedDisp.drawCourses();
}

$(document).ready(canvas_main);

