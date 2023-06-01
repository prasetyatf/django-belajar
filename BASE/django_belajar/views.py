# MAIN VIEWS
from django.shortcuts import render

def index(request):
    context = {
        'judul':'Home',
        'created_by':'Tegar'
    }
    return render(request, 'index.html', context)