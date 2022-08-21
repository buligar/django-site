from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from .models import Book
from django.views.generic import DetailView,UpdateView, DeleteView
from django.core.files.storage import FileSystemStorage


def melanomas_home(request):
    melanomas = Articles.objects.order_by('-data')
    return render(request,'melanomas/melanomas_home.html', {'melanomas': melanomas})

    # data = Book.objects.all()
    # return render(request,'melanomas/melanomas_home.html', {'data': data})

class MelanomasDetailView(DetailView):
    model = Articles
    template_name = 'melanomas/details_view.html'
    context_object_name = 'article'

class MelanomasDetailView2(DetailView):
    model = Book
    template_name = 'melanomas/details_view.html'
    context_object_name = 'book'

class MelanomasUpdateView(UpdateView):
    model = Articles
    template_name = 'melanomas/create.html'
    form_class = ArticlesForm

class MelanomasDeleteView(DeleteView):
    model = Articles
    success_url = '/melanomas'
    template_name = 'melanomas/melanomas-delete.html'


def create(request):
    error = ''
    if request.method == 'POST': #
        form = ArticlesForm(request.POST) # Получаем все данные который ввел пользователь
        if form.is_valid(): # Проверяем все данные
            form.save() # Сохраняем в базе
            return redirect('melanomas_home')
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'melanomas/create.html', data)
