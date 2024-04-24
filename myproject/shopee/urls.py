from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    path('Cart/', views.cart, name='cart'),
    path('Profile/', views.profile, name='profile'),
    path('Payments/', views.payment, name='payment'),

    ]


