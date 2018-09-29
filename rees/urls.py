from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^buy/', include('ecommerce.urls')),
    url(r'^', include('ecommerce.urls')),
]
