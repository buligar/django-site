from django.shortcuts import render,redirect
from .models import Articles
from .forms import ArticlesForm
from .models import Book
from django.views.generic import DetailView,UpdateView, DeleteView

def sites_home(request):
    sites = Articles.objects.order_by('-data')
    return render(request,'sites/sites_home.html', {'sites': sites})

    # data = Book.objects.all()
    # return render(request,'sites/sites_home.html', {'data': data})

class SitesDetailView(DetailView):
    model = Articles
    template_name = 'sites/details_view.html'
    context_object_name = 'article'

class SitesDetailView2(DetailView):
    model = Book
    template_name = 'sites/details_view.html'
    context_object_name = 'book'

class SitesUpdateView(UpdateView):
    model = Articles
    template_name = 'sites/create.html'
    form_class = ArticlesForm

class SitesDeleteView(DeleteView):
    model = Articles
    success_url = '/sites'
    template_name = 'sites/sites-delete.html'



def create(request):
    error = ''
    if request.method == 'POST' or request.method == 'GET': #
        form = ArticlesForm(request.POST, request.FILES) # Получаем все данные который ввел пользовател
        print(form.errors)
        if form.is_valid(): # Проверяем все данные
            print("Валид")
            form.save() # Сохраняем в базе
            return redirect('sites_home')
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request,'sites/create.html', data)
