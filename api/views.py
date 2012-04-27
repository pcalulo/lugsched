from django.http import *
from django.views.decorators.csrf import csrf_exempt

import markdown

# When testing with a long block of text copy-pasted from Ars Technica, Python's
# built-in unicode() function failed and threw an error. Django's smart_unicode
# function handles the same test input just fine.
from django.utils.encoding import smart_unicode

md = markdown.Markdown(safe_mode='escape')

@csrf_exempt
def markdownify_handler(request):
    # Only accept POST requests
    if request.method != 'POST':
        return HttpResponseBadRequest('<h1>HTTP 400 Bad Request</h1>')
    
    comment_text = smart_unicode(request.body)

    md.reset()
    markdowned_text = md.convert(comment_text)

    return HttpResponse(markdowned_text)
    
