


from django import forms 
from .models import Student, Blogger, MyUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UserChangeForm, PasswordResetForm,PasswordChangeForm
from django.conf import settings
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.conf import settings
from ckeditor.fields import RichTextFormField

ROLE_CHOICES = (
		('blogger','blogger'),

		('student','student'),

		)

class UserRegisterForm(UserCreationForm):
	password = forms.CharField(required=True,label='پسورد',widget=forms.PasswordInput(attrs={'class':'form-class','placeholder':'پسورد'}))
	password2 = forms.CharField(required=False,label='تکرار پسورد',widget=forms.PasswordInput(attrs={'class': 'form-class','placeholder':'تکرار پسورد'}))
	email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class' : 'form-class','placeholder':'ami@example.com'}))
	username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class' : 'form-class','placeholder':'aminghor'}))
	first_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-class','placeholder':'amin'}))
	last_name = forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-class','placeholder':'ghorbani'}))
	bio = forms.CharField(required=False,widget=forms.Textarea(attrs={'class' : 'form-class','placeholder':"چند کلمه در مورد خودتون اصافه کنین!"}))
	nickname = forms.CharField(required=False,widget=forms.TextInput(attrs={'class' : 'form-class','placeholder':'  اسمم مستعار :)'}))
	profile_image = forms.ImageField(required=False, widget=forms.FileInput)
	blogger_or_student = forms.ChoiceField(required=True,widget=forms.Select(),choices=ROLE_CHOICES)

	class Meta:
		model = MyUser
		fields = ['blogger_or_student','profile_image','nickname','username','first_name', 'email','password','password2','bio']
		#fields = '__all__'
		#exclude = ('username',)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post' # get or post
		self.helper.add_input(Submit('submit', 'Sign in')) 


	def clean_password2(self):

		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('پسورد‌ها یکی‌ نیستن دوست عزیز')
		

		return cd['password']


	def clean_email(self):
		email = self.cleaned_data['email']
		
		if not email:
			raise ValidationError("لطفا این فیلد را پر کنید")
		
		if MyUser.objects.filter(email=self.cleaned_data['email']).count():
			raise ValidationError("این ایمیل اشغال گشته.")
		
		return self.cleaned_data['email']

class UserLoginForm(AuthenticationForm):
	def __init__(self,*args, **kwargs):
		super(UserLoginForm, self).__init__(*args, **kwargs)
	
	
	
	username = forms.CharField(widget=forms.TextInput(
		attrs={'class': 'form-control', 'placeholder': 'نام کاربری تون :)', 'id': 'hello'}))
	password = forms.CharField(widget=forms.PasswordInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'رمز عبورتون :)',
			'id': 'hi',
		}
))
'''

class UserChangePasswordForm(PasswordResetForm):

	class Meta:
		model = Student
		fields = ('password',)
'''

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
		('docker', 'docker'), 
)
		
class BloggerRegisterationForm(forms.ModelForm):

	lang_experties = forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=PRO_CHOICES)
	more = forms.URLField()
	
	
	class Meta:
		model = Blogger
		exclude = ('user_blogger',)

