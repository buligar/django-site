from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
# функция для возврата картинки


urlpatterns = [
    path('', views.sites_home, name='sites_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.SitesDetailView.as_view(),name='sites-detail'),
    path('<int:pk>/update', views.SitesUpdateView.as_view(),name='sites-update'),
    path('<int:pk>/delete', views.SitesDeleteView.as_view(), name='sites-delete'),
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
