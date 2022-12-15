from .models import Articles,Book
from django.forms import ModelForm,TextInput,DateTimeInput,Textarea,ClearableFileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','full_text','data','cover','url']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'

            }),
            "url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ссылка'

            }),
            'cover':ClearableFileInput(),
        }