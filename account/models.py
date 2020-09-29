from django.db import models
from PIL import Image
from django.shortcuts import redirect, reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db.models import signals
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

def user_dir_path(instance, filename): 
  
	# file will be uploaded to MEDIA_ROOT / auth /user_<id>/<filename> 
	if instance.__class__.__name__ == 'Blogger':
		return f'media/uploads/images/acconut/{instance.__class__.__name__}/user_{instance.user_blogger.username}/{filename}'

	elif instance.__class__.__name__ == 'Student':
		 
		return f'media/uploads/images/acconut/{instance.__class__.__name__}/user_{instance.user_student.username}/{filename}'



class MyUser(AbstractUser):
	ROLE_CHOICES = (
		('student','student'),
		('blogger','blogger')

		)

	date_joined = models.DateTimeField(default=timezone.now)
	nickname = models.CharField(max_length=20,default = '',blank=True)
	bio = models.CharField(max_length=120,blank=True)
	profile_image = models.ImageField(upload_to=user_dir_path,blank=True, default=f"{settings.MEDIA_ROOT}/uploads/images/default.jpg")		
	blogger_or_student = models.CharField(max_length=25, blank=False, default='blogger', choices=ROLE_CHOICES)

	 
	def get_full_name(self):
		'''
		Returns the first_name plus the last_name, with a space in between.
		'''
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		'''
		Returns the short name for the user.
		'''
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''
		Sends an email to this User.
		'''
		send_mail(subject, message, from_email, [self.email], **kwargs) 
		
	def __str__(self):
		return self.email

	# post_save method
	@receiver(signals.post_save, sender=settings.AUTH_USER_MODEL) 
	def create_blogger_or_student(sender, instance, created, **kwargs):
		if created:
			if instance.blogger_or_student == 'blogger':
				Blogger.objects.create(user_blogger=instance)
			if instance.blogger_or_student == 'student':
				Student.objects.create(user_student=instance)

	def save(self, *args, **kwargs):
			super().save()

			img = Image.open(self.profile_image.path)
				# let's this image is more than 300 pixels

			if img.height > 300 or img.width > 300:
				output_size = (300, 300)
				img.thumbnail(output_size)
				img.save(self.profile_image.path)


class Student(models.Model):
	user_student = models.OneToOneField(MyUser, on_delete=models.CASCADE)
	is_verified = models.BooleanField(default=False, blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

	def get_absolute_url(self):

		return reverse("account:student_blogger", args =[self.user_student.username,])	


	def __str__(self):
		return self.user_student.email



class Blogger(models.Model):
	
	PRO_CHOICES = (
		('HTML', 'HTML'),
		('Css','Css'),
		('js','js'),
		('Kotlin','Kotlin'),
		('Java','java'),
		('Python','Python'),
		('C#','C#'),
		('C','C'),
		('C++','C++'),
		('Perl','Perl')
)
	user_blogger = models.OneToOneField(MyUser,on_delete=models.CASCADE)
	lang_experties = models.CharField(max_length=100, choices = PRO_CHOICES,default='C')
	more = models.URLField(max_length=1000, default='https://www.google.com', null=True, blank=True)

	def get_absolute_url(self):

		return reverse("account:profile_blogger", args =[self.user_blogger.username,])
