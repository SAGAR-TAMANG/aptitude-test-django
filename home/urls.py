from django.urls import path
from .views import Home, Questions, QuestionsTest

urlpatterns = [
    path('', Home, name='home'),
    path('questions/', Questions, name = 'questions'),
    path('questions_test/', QuestionsTest, name = 'questionstest'),
]
