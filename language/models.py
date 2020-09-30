from django.db import models
from django.urls import reverse
from django.utils import timezone
from account.models import Blogger, Student, MyUser
from ckeditor_uploader.fields import RichTextUploadingField
#from simple_history.models import HistoricalRecords
# Create your models here.

def dir_path(instance, filename): 

	# file will be uploaded to MEDIA_ROOT / auth /user_<id>/<filename>

	if instance.__class__.__name__ == 'Language':

		return f'media/uploads/images/{instance.__class__.__name__}/{instance.name}/{filename}'

	elif instance.__class__.__name__ == "Intro":

		return f'media/uploads/images/Language/{instance.__class__.__name__}/{instance.name}/{filename}'

############ ADD HELP TEXT TO EVERY ONE OF THEM ##############

############ DON"T FORGET THE VIDEO FIELD ##############

class Post(models.Model):

	STATUS_CHOICES = (
		('draft', 'در حال انتظار'),
		('published', 'منتشر شده'),
		)

	number = models.PositiveIntegerField(verbose_name='iin chandomie?',default=1)


	title = models.CharField(max_length=100,default='')

	summary = models.CharField(max_length=300,blank=True,null=True,default='')

	description = RichTextUploadingField()
	
	
	publish = models.DateTimeField(default = timezone.now, verbose_name='انتشار')
	
	created = models.DateTimeField(auto_now_add = True, verbose_name='ساخت',null=True)
	
	updated = models.DateTimeField(auto_now = True,verbose_name='آپدیت')
	
	status = models.CharField(max_length=60, choices = STATUS_CHOICES, default='draft', verbose_name='وضعیت')
	
	developed_by = models.URLField(blank=True,null=True)
	
	author = models.ForeignKey(Blogger,on_delete= models.SET_NULL,blank=True, null=True)
	

	
	is_framework = models.BooleanField(default=False)


	def author_username(self):
		#name = f'{self.author.user_blogger}'
		return 'hi' 

	#history = HistoricalRecords()
	

	def get_absolute_url(self):

		return reverse("language:lang_detail", args =[self.name,self.number])

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
 
class Language(Post):
	name = models.CharField(max_length=100, choices=PRO_CHOICES,default='HTML')
	
#	post = models.ForeignKey(Post,on_delete=models.SET_NULL,null=True)
	
	def __str__(self):
		return f'{self.name}'
	
	def parse_please(self):
		return self.title 

	def get_absolute_url(self):

		return reverse("language:lang_detail", args=[self.name,self.number])

	class Meta:
		ordering = ('created',)

class FrameWork(Post):


	name = models.CharField(max_length=50, blank=True,null=True)
	lang = models.CharField(max_length=100, choices=PRO_CHOICES,default='HTML')
		

	def __str__(self):
		
		return f'{self.lang} in {self.name} and the title {self.title}'
	


	def get_absolute_url(self):

		return reverse("language:frame_detail", args=[self.lang, self.name, self.number])


class Comment(models.Model):
	body = RichTextUploadingField(config_name='comments_bro')
	created_on = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	parent = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)
	author = models.ForeignKey(MyUser,on_delete=models.CASCADE)

	class Meta:
		ordering = ['created_on']
		abstract = True 

	def __str__(self):
		return 'Comment {} by {}'.format(self.body, self.author.username)

class CommentLanguage(Comment):	
	post = models.ForeignKey(Language,on_delete=models.CASCADE,related_name='comments')

class CommentFrameWork(Comment):	
	post = models.ForeignKey(FrameWork,on_delete=models.CASCADE,related_name='comments')
