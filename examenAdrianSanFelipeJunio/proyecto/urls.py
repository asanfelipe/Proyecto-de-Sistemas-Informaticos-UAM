from django.contrib import admin
from django.urls import path
from django.urls import include
from aplicacion import views

urlpatterns = [
    path('', views.index, name='aplicacion'),
    path('aplicacion/', include('aplicacion.urls')),
    path('admin/', admin.site.urls),
]
