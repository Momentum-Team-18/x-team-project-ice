from rest_framework import generics, permissions, filters
from django.shortcuts import render
from questions.models import Question, Answer
from questions.serializers import QuestionSerializer, AnswerSerializer


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
