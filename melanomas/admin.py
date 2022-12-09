from django.contrib import admin
from .models import Articles
from .models import Book

admin.site.register(Articles)
admin.site.register(Book)