from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.addtodo, name='add'),
    path('complete/<int:todo_pk>/', views.complete, name='complete'),
    path('delcompleted/', views.delcompleted, name='delcompleted'),
    path('delall/', views.delall, name='delall'),
]
