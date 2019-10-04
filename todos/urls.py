from django.urls import path
from todos import views
#from . import views

urlpatterns = [
    path('', views.index),

    path('new/', views.new),
    path('create/', views.create),
    
]