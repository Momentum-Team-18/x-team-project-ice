from rest_framework import generics, permissions, filters
from django.shortcuts import render
from questions.models import Question, Answer
from questions.serializers import (
    QuestionSerializer,
    AnswerSerializer,
    QuestionWithAnswerSerializer,
)
from django.core.exceptions import PermissionDenied


class QuestionViewSet(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "question_title",
        "question_author",
        "question_text",
        "question_date",
        "question_is_answered",
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(question_author=self.request.user)


class QuestionByUserViewSet(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "question_title",
        "question_author",
        "question_text",
        "question_date",
        "question is answered",
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(question_author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(question_author=self.request.user)


class AnswerByQuestionViewSet(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "id",
        "answer_text",
        "answer_author",
        "answer_date",
        "answer_author",
        "related_question",
        "answer_accepted",
    ]

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(related_question=self.request.question)

    def perform_create(self, serializer):
        serializer.save(answer_author=self.request.user)


class QuestionWithAnswerViewSet(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionWithAnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_update(self, serializer):
    #     serializer.save(answer_accepted=True)


class AcceptAnswerViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        answer = super().get_object()
        if self.request.user != answer.related_question.question_author:
            raise PermissionDenied
        serializer.save()


class UserAnswersViewSet(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.queryset.filter(answer_author=self.request.user)
