import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body # string of JSON data
    data = {}
    
    try: data = json.loads(body) # string of JSON data turnt into data dictionary
    except: pass
    
    data['params'] = dict(request.GET)
    data['content_type'] = request.content_type
    
    return JsonResponse(data)