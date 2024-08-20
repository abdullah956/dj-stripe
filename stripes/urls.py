# urls.py
from django.shortcuts import render
from django.urls import path
from .views import create_checkout_session,checkout_view,success_view,cancel_view
urlpatterns = [
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('checkout/', checkout_view, name='checkout'),
    path('success/', success_view, name='success'),
    path('cancel/', cancel_view, name='cancel'),
]
