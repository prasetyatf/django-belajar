from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sitemap(request):
    return render(request, 'sitemap/index.html')

def blog(request):
    return render(request, 'blog/index.html')


