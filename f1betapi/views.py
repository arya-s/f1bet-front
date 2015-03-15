from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import Http404

@csrf_exempt
def index(request):

    if request.method == 'POST':
        return JsonResponse({ 'ok': 'vettel' })

    return Http404