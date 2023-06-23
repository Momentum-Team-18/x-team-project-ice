from rest_framework import generics, permissions, filters
from django.shortcuts import render
from questions.models import Question
from questions.serializers import QuestionSerializer


class QuestionViewSet(generics.ListCreateAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['question_title', 'question_author',
                     'question_text', 'question_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(question_author=self.request.user)
