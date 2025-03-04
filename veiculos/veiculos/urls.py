from django.contrib import admin
from django.urls import path, include
from carros.urls import router
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include('carros.urls')),
    
]

# para carregar os uploads
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)