from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.ListQuestions.as_view()),
    path('create/', views.CreateQuestions.as_view()),
    path('update/<int:pk>/',views.UpdateorDeleteQuestion.as_view()),
    path('delete/<int:pk>/', views.UpdateorDeleteQuestion.as_view())
]
