
function isInputComplete() {
    form = document.forms["courseData"]
    if (form.courseCode.value == '')
        return false;
    if (form.courseName.value == '')
        return false;

    // Let's consider the course description as optional - don't check it

    return true;
}

function doInputValidation()
{
    complete = isInputComplete();

    if (!complete) {
        $("#data-incomplete-message").slideDown()
    }

    return complete;
}

