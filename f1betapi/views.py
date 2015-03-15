from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import Http404

import json

@csrf_exempt
def index(request):

    if request.method == 'POST':

        data = json.load(request.body)
        print data

        return JsonResponse({ 'data': 'unkown driver'})


    return Http404