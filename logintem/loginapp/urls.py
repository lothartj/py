from django.urls import path
from loginapp import views

urlpatterns = [
    path('', views.login, name='login')
]
