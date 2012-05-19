
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

function disableCommentWidgets() {
    $("#comment-input > textarea").attr("disabled", true);
    $("#comment-input > .controls > input").attr("disabled", true);
}

function enableCommentWidgets() {
    $("#comment-input > textarea").attr("disabled", false);
    $("#comment-input > .controls > input").attr("disabled", false);
}

function getPreview() {
    // Disable potentially pesky buttons, and show the "getting preview" message
    disableCommentWidgets();
    $("#comment-input > .controls > .preview-controls").show();

    // Send the text to the server for markdownifying
    var text = $("#comment-box").val();
    console.log("Previewing: " + text);
    $.ajax({
        url: '/api/misc/markdownify',
        data: text,
        type: 'POST',
        processData: false,
        success: function(data, textStatus, jqXHR) {
            console.log(textStatus);
            if (textStatus == "success") {
                $("#comment-preview").html(data).slideDown();
                $("#comment-box").slideUp();
                $("#comment-input > .controls > .preview-controls").hide();
                $("#comment-input > .controls > input[name=get-preview]")
                    .hide();
                $("#comment-input > .controls > input[name=close-preview]")
                    .show().attr("disabled", false);
            }
        },
        dataType: 'html'
    })
}

function cancelPreview() {
    // Re-enable buttons that were disabled, and hide the "getting preview"
    // message
    enableCommentWidgets()
    $("#comment-input > .controls > .preview-controls").hide();

    // Abort the request
    if (previewJqXHR) {
        previewJqXHR.abort();
        previewJqXHR = null;
    }
}

function closePreview() {
    enableCommentWidgets();
    $("#comment-input > textarea").slideDown();
    $("#comment-preview").slideUp();
    $("#comment-input > .controls > input[name=close-preview]")
        .hide()
    $("#comment-input > .controls > input[name=get-preview]")
        .show();
}

function postComment() {
    var text = $("#comment-input > textarea").val()
    $.ajax({
        url: 'comments',
        data: text,
        type: 'POST',
        processData: false,
        success: function(data, textStatus, jqXHR) {
            console.log(textStatus);
            console.log(data);
        },
        dataType: 'html'
    })
}


///////////////////////////////////////////////////////////////////////
// "Add Section" panel
///////////////////////////////////////////////////////////////////////
AddSectionPanel = {}

AddSectionPanel.show = function() {
    $("#add-section-toggle").text("Cancel");
    $("#add-section-panel").slideDown();
}

AddSectionPanel.hide = function() {
    $("#add-section-toggle").text("Add Section");
    $("#add-section-panel").slideUp();
}

AddSectionPanel.toggle = function() {
    if (!$("#add-section-panel").is(":visible")) {
        AddSectionPanel.show();
    } else {
        AddSectionPanel.hide();
    }
}

