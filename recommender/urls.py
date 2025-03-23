from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.quiz, name='quiz'),
    path('reset_quiz/', views.reset_quiz, name='reset_quiz'),
    path('shoes/', views.shoe_list, name='shoe_list'),
    path('shoes/<int:shoe_id>/', views.shoe_detail, name='shoe_detail'),
]
