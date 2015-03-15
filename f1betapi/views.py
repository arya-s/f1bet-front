from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import Http404

import json

@csrf_exempt
def index(request):

    if request.method == 'POST':

        print request.body


        return JsonResponse({ 'driver': 'vettel' })

    return Http404