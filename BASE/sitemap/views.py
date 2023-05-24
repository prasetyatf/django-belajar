from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'sitemap/index.html')

def blog(request):
    return HttpResponse('Ini blog')

def about(request):
    return HttpResponse('Ini About')

def sitemap(request):
    return HttpResponse('Ini Sitemap')
