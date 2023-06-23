from django.contrib import admin
from questions.models import User, Question, Answer
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
