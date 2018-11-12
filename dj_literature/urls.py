from django.urls import path

from . import views

# todo 还有好多没有做
urlpatterns = [
    path('', views.index, name='index'),
]
