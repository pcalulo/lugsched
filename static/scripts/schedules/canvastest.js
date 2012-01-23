
function canvas_main() {
    var schedDisp = new ScheduleDisplay(document.getElementById("chart-canvas"));
    var course = new Course();
    course.section.meetings[0].endTime.setHours(10);
    course.section.meetings[0].endTime.setMinutes(0);
    schedDisp.addCourse(course);

    course = new Course();
    course.code = 'HIWRLD';
    course.section.meetings[0].startTime.setHours(13);
    course.section.meetings[0].endTime.setHours(14);
    course.section.meetings[0].hasThursdays = true;
    schedDisp.addCourse(course)

    schedDisp.drawCourses();
}

$(document).ready(canvas_main);

