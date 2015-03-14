from django.shortcuts import render

from models import RedditUser

def index(request):

    return render(request, 'index.html', { "v": "ok" })