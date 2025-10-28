from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('memes/', views.memes, name='memes'),
]