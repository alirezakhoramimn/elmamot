from django.urls import path, include
from . import views 

app_name = 'quiz'

urlpatterns = [
    path('questionframe/',views.QuestionPostFrameCreateView,name='questionframe'),
    path('questionlang/',views.QuestionPostLangCreateView,name='questionlang'),
    path('questionframe/update',views.QuestionPostFrameUpdateView,name='questionframe-update'),
    path('questionlang/update',views.QuestionPostLangUpdateView,name='questionlang-update'),

]
