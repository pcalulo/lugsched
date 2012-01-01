
function canvas_main() {
    var canvas = document.getElementById('tutorial');
    var ctx = canvas.getContext('2d');

    // Draw vertical lines
    for (var i = 20; i <= 620; i += 100) {
        ctx.beginPath();
        ctx.moveTo(i + 0.5, 20);
        ctx.lineTo(i + 0.5, 420);
        ctx.stroke();
    }

    // Draw header border lines
    for (var i = 0; i <= 32; i += 32) {
        ctx.beginPath()
        ctx.moveTo(20.5, i + 20.5);
        ctx.lineTo(620.5, i + 20.5);
        ctx.stroke();
    }
}

$(document).ready(canvas_main);

