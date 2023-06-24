from django.urls import path, include
from questions import views


urlpatterns = [
    path("questions/", views.QuestionViewSet.as_view(), name="questions"),
    path(
        "questions/user/", views.QuestionByUserViewSet.as_view(), name="user_questions"
    ),
    path("questions/answer/", views.AnswerByQuestionViewSet.as_view(), name="answers"),
    path(
        "questions/<int:pk>/",
        views.QuestionWithAnswerViewSet.as_view(),
        name="question_details",
    ),
]
