from django.urls import path, include
from questions import views


urlpatterns = [
    path('questions/', views.QuestionViewSet.as_view(), name='questions'),

]
