from rest_framework import viewsets, permissions, filters
from django.shortcuts import render
from questions.models import Question
from questions.serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['question_title', 'question_author',
                     'question_text', 'question_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
