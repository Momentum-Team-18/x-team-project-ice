from rest_framework import serializers
from questions.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["id", "question_title", "question_text", "question_author"]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            "id",
            "answer_text",
            "answer_author",
            "answer_date",
            "answer_author",
            "related_question",
            "answer_accepted",
        ]
