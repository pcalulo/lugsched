
function toggleMarkdownHelp() {
    var mdhelp = $("#markdown-help");

    if (mdhelp.is(":visible")) {
        mdhelp.slideUp();
        $("#markdown-toggle").text("Formatting help");
    } else {
        mdhelp.slideDown();
        $("#markdown-toggle").text("Close formatting help");
    }
}

function getPreview() {
    var text = $("#comment-box").val();
    console.log("Previewing: " + text);
    data = {}
    data.text = text
    $.get('./preview', data, function(data, textStatus, jqXHR) {
        console.log(data);
    });
}

