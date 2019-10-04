from django.urls import path
from todos import views
#from . import views

app_name= 'todos'

urlpatterns = [
    path('', views.index, name="index"),

    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    
    path('<int:id>/delete/', views.delete, name="delete"),
]