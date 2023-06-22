from rest_framework import serializers
from questions.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        models = Question
        fields = ['url', 'question_title', 'question_text',
                  'question_author', 'question_date', 'question_is_answered']
