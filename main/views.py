from django.shortcuts import render



def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some','Hello','123'],
        'obj': {
            'my': 'admin',
            'new': 1,
            'friend': 'Buligar'
        }
    }
    return render(request,'main/index.html',data)

def about(request):
    return render(request,'main/about.html')


