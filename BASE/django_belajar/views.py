# MAIN VIEWS
from django.shortcuts import render

def index(request):
    context = {
        'judul':'Home',
        'created_by':'Tegar',
        'header':'<h1>Ini header</h1>',
        'footer':'<h1>Ini footer</h1>',
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/sitemap', 'Sitemap'],
        ],
        'about':[
            ['Nama:', 'Tegar'],
            ['Hobi:', 'Ngoding']
        ]
    }
    return render(request, 'index.html', context)