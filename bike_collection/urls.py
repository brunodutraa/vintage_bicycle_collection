from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('colecao/', include('collection.urls')),
    path('', index, name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
