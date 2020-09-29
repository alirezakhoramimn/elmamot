from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(QuestionFrameAll)
admin.site.register(QuestionFramePost)
admin.site.register(QuestionLangAll)
admin.site.register(QuestionLangPost)
admin.site.register(AnswerFrameAll)
admin.site.register(AnswerFramePost)
admin.site.register(AnswerLangAll)
admin.site.register(AnswerLangPost)