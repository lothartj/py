from . import views
from django.urls import path

urlpatterns = [
   path('main/', views.main, name='main' ),
   path('', views.user_login, name='login'),
   path('itemview/', views.itemview, name='itemview'),
   path('itemitself/<int:item_id>/', views.itemitself, name='itemitself'),
   path('delteitem/<int:item_id>/', views.itemdelete, name='itemdelete')
]
