
// The jqXHR returned by jQuery for the preview request
var previewJqXHR;

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
    // Disable potentially pesky buttons, and show the "getting preview" message
    $("#comment-input > textarea").attr("disabled", true);
    $("#comment-input > .controls > input").attr("disabled", true);
    $("#comment-input > .controls > .preview-controls").show();

    // Send the text to the server for markdownifying
    var text = $("#comment-box").val();
    console.log("Previewing: " + text);
    $.ajax({
        url: './preview',
        data: text,
        type: 'POST',
        processData: false,
        success: function(data, textStatus, jqXHR) {
            console.log(data);
        },
        dataType: 'html'
    })
}

function cancelPreview() {
    // Re-enable buttons that were disabled, and hide the "getting preview"
    // message
    $("#comment-input > textarea").attr("disabled", false);
    $("#comment-input > .controls > input").attr("disabled", false);
    $("#comment-input > .controls > .preview-controls").hide();

    // Abort the request
    if (previewJqXHR) {
        previewJqXHR.abort();
        previewJqXHR = null;
    }
}

