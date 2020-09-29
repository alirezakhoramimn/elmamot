from django import forms 
from .models import QuestionFramePost, QuestionLangPost
from account.models import Blogger 
from ckeditor.widgets import CKEditorWidget

ANSWER_CHOICES = (
        (1,1),
        (2,2),
        (3,3),
        (4,4)
    )


class QuestionFrameForm(forms.ModelForm):


    title = forms.CharField()
    question = forms.CharField(widget = CKEditorWidget,required=True, label='sooaal!')
    answer = forms.ChoiceField(required=True,widget=forms.Select(),choices=ANSWER_CHOICES)
	
    class Meta:
        model = QuestionFramePost
        fields = ('title','question','answer', 'frame')

class QuestionLangForm(forms.ModelForm):


    title = forms.CharField()
    question = forms.CharField(widget = CKEditorWidget,required=True, label='sooaal!')
    answer = forms.ChoiceField(required=True,widget=forms.Select(),choices=ANSWER_CHOICES)
	
    class Meta:
        model = QuestionLangPost
        fields = ('title','question','answer', 'lang')