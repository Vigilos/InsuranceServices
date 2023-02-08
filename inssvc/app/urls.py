from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product1/', views.product1, name='product1'),
    path('product2/', views.product2, name='product2'),
    path('product3/', views.product3, name='product3'),
]
