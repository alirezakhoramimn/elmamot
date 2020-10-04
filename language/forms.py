from django import forms
from .models import Language, FrameWork, CommentFrameWork,CommentLanguage 
from account.models import Blogger 
from ckeditor_uploader.widgets import CKEditorUploadingWidget

PRO_CHOICES = (
		('HTML5', 'HTML'),
		('Bootstrap4','Bootstrap4'),
		('Css3','Css3'),
		('Js','js'),
		('Kotlin','Kotlin'),
		('Java','java'),
		('C++','C++'),
		('Perl','Perl'),
		('C-Sharp', 'C-Sharp'),
		('Python', 'Python'),
		('GraphQL', 'GraphQL'),
		('REST', 'REST'),
		('PostgreSQL', 'PostgreSQL'),
		('MySQL', 'MySQL'),
		('SQLServer','SQLServer'),
		('linux', 'linux'),
		('git','git'),
		('ducker', 'ducker'), 
)
 

class LangCreateForm(forms.ModelForm):
	
	number = forms.IntegerField()
	
	name = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control '}),choices=PRO_CHOICES)
	
	description = forms.CharField(label='man babatam ',required=True,widget=CKEditorUploadingWidget())
	
	title =forms.CharField(required=True,max_length=100,widget=forms.TextInput(  
		attrs={
			'class': 'form-control ',
			'placeholder': 'تایتل',
			'id': 'hi',
		}))

	summary =forms.CharField(required=False,max_length=150,widget=forms.Textarea(
		attrs={
			'class':"form-control ",
			'placeholder': 'لطفا یک خلاصه ای از این مقاله بزار در حد ۱۵ - 20 کلمه '
		}
	))

	developed_by = forms.URLField(required=False,widget=forms.URLInput(
		attrs = {
			'class': 'form-control '
		}
	))



	#
	# is_framework = forms.BooleanField()
	class Meta:
		model = Language
		fields = ('title','number', 'summary', 'developed_by', 'description','name')




class FrameCreateForm(forms.ModelForm):
	name = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=PRO_CHOICES)
	

	description = forms.CharField(required=True,widget=CKEditorUploadingWidget())
	
	title =forms.CharField(required=True,max_length=100,widget=forms.TextInput())

	summary =forms.CharField(required=False,max_length=300,widget=forms.TextInput())

	developed_by = forms.URLField(required=False,widget=forms.URLInput())
	
	lang = forms.ChoiceField(required=True,widget=forms.Select(),choices=PRO_CHOICES)

	#is_framework = forms.BooleanField()
	class Meta:
		model = FrameWork		
		fields = ('title','number','summary', 'developed_by', 'description','name','lang')


class CommentFrameWorkForm(forms.ModelForm):
	body = forms.CharField(max_length=600,required=True, widget=CKEditorWidget(config_name='comments_bro',attrs={'class':'form-control'}))

	class Meta:
		model = CommentFrameWork
		fields = ('body',)

class CommentLanguageForm(forms.ModelForm):
	body = forms.CharField(max_length=600,required=True, widget=CKEditorWidget(config_name='comments_bro',attrs={'class':'form-control'}))

	class Meta:
		model = CommentLanguage
		fields = ('body',)

class SearchForm(forms.ModelForm):
	query = forms.CharField(max_length=60)
