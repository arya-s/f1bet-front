from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import Http404

import json

@csrf_exempt
def index(request):

    if request.method == 'POST':

        data = json.loads(request.body)
        print data

        if data.get('driver') == 'vettel'
            return JsonResponse({ 'pos': '3' })
        else
            return JsonResponse({ 'data': 'unkown driver'})


    return Http404