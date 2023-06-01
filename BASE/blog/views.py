from django.shortcuts import render

def index(request):
    context = {
        'judul':'Blog',
        'created_by':{'nama':'Tegar', 'umur':26},
        'contributor':[
            ['Prasetya',27],
            ['Aji',28]
        ]
    }
    return render(request, 'blog/index.html', context)
