from django.urls import path

from file import views

urlpatterns = [
    path('upload1', views.upload1, name='upload1'),
    path('upload2', views.upload2, name='upload2'),
    path('login/<str:id>', views.login, name='login'),
    path('download', views.download, name='download'),
]
