from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('google/', views.google, name='google'),
    path('dropbox/', views.dropbox, name='dropbox')
]
