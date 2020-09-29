from django.db import models
from django.conf import settings
from account.models import Blogger, Student
from django.shortcuts import redirect, reverse
from language.models import Language, FrameWork

from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
ANSWER_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
    )

class QuestionFrameAll(models.Model):
 

    title =  models.CharField(max_length=35)
    question = RichTextUploadingField()
    user = models.ForeignKey(Blogger,
                            on_delete=models.CASCADE, 
                            )
    created = models.DateTimeField(auto_now_add=True)

    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)


    def __str__(self):
        return f'{self.title} with answer of {self.answer}'
    
class AnswerFrameAll(models.Model):
    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)
    question = models.ForeignKey(QuestionFrameAll, on_delete=models.SET_DEFAULT, default=' ')
    user = models.ForeignKey(Student, on_delete=models.CASCADE,null=True )

    def __str__(self):
        return self.answer

class QuestionFramePost(models.Model):
    question = RichTextUploadingField()
    frame = models.ForeignKey(FrameWork, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)


    class Meta:
        verbose_name = ("QuestionFrameSpecfic")
  

    def __str__(self):
        return f'{self.title} for the {frame.title}'
    
class AnswerFramePost(models.Model):
    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)
    question = models.ForeignKey(QuestionFramePost, on_delete=models.SET_DEFAULT, default=' ')
    user = models.ForeignKey(Student, on_delete=models.CASCADE,null=True )

    def __str__(self):
        return self.answer
  #  def get_absolute_url(self):
 
    #    return reverse("language:frame_detail", args=[self.lang, self.name, self.slug])

  
class QuestionLangAll(models.Model):
 

    title =  models.CharField(max_length=35)
    question = RichTextUploadingField()
    user = models.ForeignKey(Blogger,
                            on_delete=models.CASCADE, 
                            )
    created = models.DateTimeField(auto_now_add=True)

    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)


    def __str__(self):
        return f'{self.title} with answer of {self.answer}'
    

class AnswerLangAll(models.Model):
    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)
    question = models.ForeignKey(QuestionLangAll, on_delete=models.SET_DEFAULT, default=' ')
    user = models.ForeignKey(Student, on_delete=models.CASCADE,null=True )

    def __str__(self):
        return self.answer


class QuestionLangPost(models.Model):
    question = RichTextUploadingField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)


    class Meta:
        verbose_name = ("QuestionLangSpecifc")
        

    def __str__(self):
        return f'{self.title} for the {self.lang.title}'
    

   # def get_absolute_url(self):
   #     return reverse("quiz:lang_detail", args=[self.name, self.slug])
class AnswerLangPost(models.Model):
    answer = models.CharField(choices=ANSWER_CHOICES,max_length=1)
    question = models.ForeignKey(QuestionLangPost, on_delete=models.SET_DEFAULT, default=' ')
    user = models.ForeignKey(Student, on_delete=models.CASCADE,null=True )

    def __str__(self):
        return self.answer