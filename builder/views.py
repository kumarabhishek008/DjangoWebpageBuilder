from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pages
from django.core.serializers import serialize
import json

# Create your views here.

def index(request):
    return render(request, 'index.html')

def savePage(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        page = Pages.objects.create(name="untitled", html=html, css=css)
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]}) 