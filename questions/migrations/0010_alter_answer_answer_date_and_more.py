# Generated by Django 4.2.2 on 2023-06-26 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_alter_answer_answer_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 15, 42, 18, 730232, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 26, 15, 42, 18, 727811, tzinfo=datetime.timezone.utc)),
        ),
    ]