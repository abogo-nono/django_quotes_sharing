from django.urls import path
from . import views

urlpatterns = [
    path('', views.quote_list, name='quote_list'),
    path('add/', views.add_quote, name='add_quote'),
]
