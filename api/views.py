from django.http import *
from django.views.decorators.csrf import csrf_exempt

import markdown

md = markdown.Markdown(safe_mode='escape')

@csrf_exempt
def markdownify_handler(request):
    # Only accept POST requests
    if request.method != 'POST':
        return HttpResponseBadRequest('<h1>HTTP 400 Bad Request</h1>')
    
    comment_text = str(request.body)

    print 'REQUEST BODY: ', comment_text

    md.reset()
    markdowned_text = md.convert(comment_text)

    return HttpResponse(markdowned_text)
    
