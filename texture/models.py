from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')
    book = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title