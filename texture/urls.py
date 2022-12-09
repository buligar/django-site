from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# функция для возврата картинки
from .views import home_page

urlpatterns = [
    path('', views.texture_home, name='texture_home'),
    path('', home_page)
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)