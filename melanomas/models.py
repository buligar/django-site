from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    data = models.DateTimeField('Дата публикации')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/melanomas/{self.id}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    # def table(self):
    #     table=open('glcm')

class Book(models.Model):
    title = models.CharField(max_length=150)
    book = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title