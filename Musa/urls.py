from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
	path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/',include("rest_framework.urls")),
    path('ckeditor/',include("ckeditor_uploader.urls")),
   	path('api/v1/',include("MDShop.urls")),
   	
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)