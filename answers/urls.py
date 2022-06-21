from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListAnswers.as_view()),
    path('create/', views.CreateAnswer.as_view()),
    path('update/<int:pk>/',views.UpdateorDeleteAnswer.as_view()),
    path('delete/<int:pk>/', views.UpdateorDeleteAnswer.as_view())
]

