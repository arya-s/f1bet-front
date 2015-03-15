from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import Http404

@csrf_exempt
def index(request):

    response = dict()

    payload = request.POST.get('payload', None)
    if payload is None:
        raise Http404

    data = payload.get('data', None)
    if data:
        driver = data.get('driver')

        if driver == 'Vettel':
            response['position'] = 3

    return JsonResponse(response)