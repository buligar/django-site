from django.shortcuts import render,redirect
from .models import Book
from django.core.files.storage import FileSystemStorage


def texture_home(request):
    data = Book.objects.all()
    return render(request,'texture/texture.html', {'data': data})

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


def home_page(request):
    # POST - обязательный метод
    if request.method == 'POST' and request.FILES:
        # получаем загруженный файл
        file = request.FILES['myfile1']
        fs = FileSystemStorage()
        # сохраняем на файловой системе
        filename = fs.save(file.name, file)
        # получение адреса по которому лежит файл
        file_url = fs.url(filename)
        return render(request, 'texture/texture.html', {
            'file_url': file_url
        })
    return render(request, 'texture/texture.html')