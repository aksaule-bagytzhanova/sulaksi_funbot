from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('random_words/', views.RandomWord.as_view(), name='random_english_word'),

]