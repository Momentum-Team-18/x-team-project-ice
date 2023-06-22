from rest_framework import serializers
from questions.models import Question, User


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['url', 'question_title', 'question_text',
                  'question_date', 'question_is_answered']
