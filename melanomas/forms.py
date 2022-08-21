from .models import Articles,Book
from django.forms import ModelForm,TextInput,DateTimeInput,Textarea,FileInput


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons','full_text','data','images']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название изображения'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс изображения'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'

            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание изображения'
            }),
            "images": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавить изображения'
            }),
        }