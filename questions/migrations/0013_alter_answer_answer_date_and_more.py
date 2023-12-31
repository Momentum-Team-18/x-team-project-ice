# Generated by Django 4.2.2 on 2023-06-27 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("questions", "0012_alter_answer_answer_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="answer_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 27, 14, 43, 12, 1108, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="question",
            name="question_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 6, 27, 14, 43, 12, 737, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
