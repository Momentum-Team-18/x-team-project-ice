from django.urls import path, include
from questions import views


urlpatterns = [
    # GET|POST
    path("questions/", views.QuestionViewSet.as_view(), name="questions"),
    # GET
    path(
        "questions/user/", views.QuestionByUserViewSet.as_view(), name="user_questions"
    ),
    # GET|POST
    path("questions/answer/", views.AnswerByQuestionViewSet.as_view(), name="answers"),
    # GET
    path("questions/<int:pk>/", views.QuestionWithAnswerViewSet.as_view(),
         name="question_details"),
    # PATCH
    path("answers/accept/<int:pk>/",
         views.AcceptAnswerViewSet.as_view(), name="accept_answer"),
    # GET
    path("answers/user/",
         views.UserAnswersViewSet.as_view(), name="user_answers"),
    # DELETE
    path("questions/delete/<int:pk>/",
         views.DeleteQuestionViewSet.as_view(), name="delete_question"),
]
