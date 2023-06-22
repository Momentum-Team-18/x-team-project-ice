# Generated by Django 4.2.2 on 2023-06-22 19:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=250)),
                ('question_text', models.TextField()),
                ('question_date', models.DateTimeField(default=datetime.datetime(2023, 6, 22, 19, 28, 51, 803679, tzinfo=datetime.timezone.utc))),
                ('question_is_answered', models.BooleanField(default=False)),
                ('question_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-question_date'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('answer_date', models.DateTimeField(default=datetime.datetime(2023, 6, 22, 19, 28, 51, 804445, tzinfo=datetime.timezone.utc))),
                ('answer_accepted', models.BooleanField(default=False)),
                ('answer_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('related_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.question')),
            ],
            options={
                'ordering': ['-answer_date'],
            },
        ),
    ]
