import datetime
from django.contrib import admin
from .models import Question,Choice
from django.utils import timezone

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    # fields = ['pub_date', 'question_text']

    list_display = ('question_text'
                    ,'pub_date'
                    # ,'was_published_recently' --??为什么报错
    )
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)