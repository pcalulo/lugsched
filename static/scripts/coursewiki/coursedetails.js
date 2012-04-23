
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

