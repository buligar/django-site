from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# функция для возврата картинки

urlpatterns = [
    path('', views.melanomas_home, name='melanomas_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.MelanomasDetailView.as_view(),name='melanomas-detail'),
    path('<int:pk>/update', views.MelanomasUpdateView.as_view(),name='melanomas-update'),
    path('<int:pk>/delete', views.MelanomasDeleteView.as_view(), name='melanomas-delete'),
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
