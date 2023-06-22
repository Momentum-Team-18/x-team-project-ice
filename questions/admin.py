from django.contrib import admin
from questions.models import User, Question
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Question)
