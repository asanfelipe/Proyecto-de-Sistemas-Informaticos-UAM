from django.urls import path
from aplicacion import views

app_name = 'aplicacion'

urlpatterns = [
    path('', views.index, name='aplicacion'),
    path('usuario/', views.index, name='usuario'),
]
