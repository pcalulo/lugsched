
var GRID_COL_WIDTH = 120;

// Ensure that lines are aligned with pixels.
// See https://developer.mozilla.org/en/Canvas_tutorial%3AApplying_styles_and_colors#A_lineWidth_example
var X_OFFSET = 45.5;
var Y_OFFSET = 5.5;

var TIME_MARKER_BASE_Y = Y_OFFSET + 52;

function ScheduleDisplay(canvas) {
    if (!canvas) {
        console.error("Must pass a canvas into ScheduleDisplay!");
        return;
    }

    // Check for canvas support
    if (!this.isCanvasSupported()) {
        console.log("Canvas is not supported by this browser.");
        return;
    }

    this.canvas = canvas;

    // In case I carelessly use something like $("#chart-canvas") again...
    // (JQuery returns an array of matching objects, even if you give it an
    // ID and there's only one possible result)
    if (!canvas.getContext) {
        console.error('Object passed into ScheduleDisplay constructor is not a canvas!');
        return;
    }

    // Yay, this browser supports canvas!
    // Get the context and get to work.
    this.ctx = canvas.getContext('2d');
    this.drawChart();
}

ScheduleDisplay.prototype.isCanvasSupported = function() {
    // This is from http://stackoverflow.com/questions/2745432/best-way-to-detect-that-html5-canvas-is-not-supported
    var elem = document.createElement('canvas');
    return !!(elem.getContext && elem.getContext('2d'));
}

ScheduleDisplay.prototype.drawDayHeaders = function() {
    var days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var ctx = this.ctx;
    // Save context, so we don't mess up anyone else's draws to the canvas
    // (similar to PUSHA in x86 assembly)
    ctx.save();

    ctx.font = '12pt Droid Sans';
    for (var i = 0; i < days.length; i++) {
        ctx.fillText(days[i], X_OFFSET + 10 + (GRID_COL_WIDTH * i), Y_OFFSET + 22);
    }

    // Restore the context we saved earlier, so the caller won't be using a
    // canvas context with settings changed out from under them
    // (similar to POPA in x86 assembly)
    ctx.restore();
}

// TODO: Only show time on class start/end points?
ScheduleDisplay.prototype.drawTimeMarkers = function() {
    var times = [
        '8:00am', '9:00am', '10:00am', '11:00am', '12:00nn', '1:00pm', '2:00pm',
        '3:00pm', '4:00pm', '5:00pm', '6:00pm', '7:00pm'
    ];
    var ctx = this.ctx;

    // Save context, so we don't mess up anyone else's draws to the canvas
    // (similar to PUSHA in x86 assembly)
    ctx.save();

    ctx.font = '8pt Droid Sans';
    ctx.textAlign = 'right';

    for (var i = 0; i < times.length; i++) {
        // Time markers are 40px apart
        ctx.fillText(times[i], X_OFFSET - 3, TIME_MARKER_BASE_Y + (40 * i));
    }

    // Restore the context we saved earlier, so the caller won't be using a
    // canvas context with settings changed out from under them
    // (similar to POPA in x86 assembly)
    ctx.restore();
}

ScheduleDisplay.prototype.createDummyCourses = function() {

}

ScheduleDisplay.prototype.drawCourses = function(courses) {
    
}

ScheduleDisplay.prototype.drawChart = function() {
    var ctx = this.ctx;
    var days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

    ctx.save();
    ctx.strokeStyle = '#BBBBBB';

    // Draw vertical lines
    for (var i = 0; i <= days.length; i++) {
        ctx.beginPath();
        ctx.moveTo((i * GRID_COL_WIDTH) + X_OFFSET, Y_OFFSET);
        ctx.lineTo((i * GRID_COL_WIDTH) + X_OFFSET, 510)
        ctx.stroke();
    }

    // Draw header border lines
    for (var i = 0; i <= 32; i += 32) {
        ctx.beginPath()
        ctx.moveTo(X_OFFSET, i + Y_OFFSET);
        ctx.lineTo(X_OFFSET + (GRID_COL_WIDTH * days.length), i + Y_OFFSET);
        ctx.stroke();
    }


    // For development - an easy way to tell how far we are from the canvas's edge
    ctx.beginPath()
    ctx.moveTo(0, Y_OFFSET);
    ctx.lineTo(X_OFFSET, Y_OFFSET);
    ctx.stroke();

    this.drawDayHeaders();
    this.drawTimeMarkers();

    // Let's see how this thing would look...
    ctx.fillStyle = "rgba(190, 255, 190, 0.5)"
    ctx.fillRect(X_OFFSET, TIME_MARKER_BASE_Y - 8, GRID_COL_WIDTH, 60);

    ctx.restore()
}

