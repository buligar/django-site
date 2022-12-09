from django.db import models

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format('images/', filename)

class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата публикации')
    print(user_directory_path)
    cover = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/melanomas/{self.id}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    # def table(self):
    #     table=open('glcm')

class Book(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title


# posts/models.py
from django.db import models


