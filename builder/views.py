from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Pages
from django.core.serializers import serialize
import json

# Create your views here.

def index(request):
    pages = Pages.objects.all()
    return render(request, 'pages.html', { "pages": pages })

def addPage(request):
    return render(request, 'index.html')

def savePage(request):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        page = Pages.objects.create(name="untitled", html=html, css=css)
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]}) 

def editPage(request, id):
    page = Pages.objects.get(pk=id)
    return render(request, 'index.html', {"page": page})

def editPageContent(request, id):
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        page = Pages.objects.get(pk=id)
        page.html = html
        page.css = css
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]})    

def previewPage(request, id):
    page = Pages.objects.get(pk=id)
    return render(request, 'preview.html', {"page": page})