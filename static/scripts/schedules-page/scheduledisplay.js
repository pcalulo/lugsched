
var GRID_COL_WIDTH = 120;
var X_OFFSET = 45.5;
var Y_OFFSET = 5.5;

function ScheduleDisplay(canvas) {
    if (!canvas) {
        console.error("Must pass a canvas into ScheduleDisplay!");
    }

    this.canvas = canvas;

    // Check for canvas support
    if (canvas.getContext) {
        this.canvasSupported = true;
    } else {
        console.log("Canvas is not supported by this browser.");
        this.canvasSupported = false;
        return;
    }

    this.ctx = canvas.getContext('2d');
    this.drawChart();
}

ScheduleDisplay.prototype.isCanvasSupported = function() {
    return this.canvasSupported;
}

ScheduleDisplay.prototype.drawChart = function() {
    var ctx = this.ctx;
    var days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];

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

    ctx.beginPath()
    ctx.moveTo(0, Y_OFFSET);
    ctx.lineTo(X_OFFSET, Y_OFFSET);
    ctx.stroke();

    // Draw text
    ctx.font = '12pt Droid Sans';
    for (var i = 0; i < days.length; i++) {
        ctx.fillText(days[i], X_OFFSET + 10 + (GRID_COL_WIDTH * i), Y_OFFSET + 22);
    }

    ctx.font = '8pt Droid Sans';
    ctx.textAlign = 'right';
    ctx.fillText("8:00am", 43, 57);
    ctx.fillText("9:00am", 43, 97);
    ctx.fillText("10:00am", 43, 137);
    ctx.fillText("11:00am", 43, 177);
    ctx.fillText("12:00nn", 43, 217);
    ctx.fillText("1:00pm", 43, 257);
    ctx.fillText("2:00pm", 43, 297);
    ctx.fillText("3:00pm", 43, 337);
    ctx.fillText("4:00pm", 43, 377);
    ctx.fillText("5:00pm", 43, 417);
    ctx.fillText("6:00pm", 43, 457);
}

