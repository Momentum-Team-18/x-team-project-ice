from rest_framework import serializers
from questions.models import Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    question_author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "question_author",
            "question_title",
            "question_text",
            "question_is_answered",
        ]


class AnswerSerializer(serializers.ModelSerializer):
    answer_author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Answer
        fields = [
            "id",
            "answer_author",
            "answer_text",
            "answer_author",
            "answer_date",
            "related_question",
            "answer_accepted",
        ]


class QuestionWithAnswerSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = [
            "id",
            "question_title",
            "question_text",
            "question_author",
            "question_is_answered",
            "answers",
        ]
