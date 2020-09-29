from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm
from .models import Student,Blogger, MyUser

'''
class CustomUserAdmin(UserAdmin):
    add_form = StudentCreationForm
    form = StudentChangeForm
    model = Student
    list_display = ['email', 'username',]

admin.site.register(CustomUser, CustomUserAdmin)

'''


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
	list_display = ['user_blogger']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['user_student']


@admin.register(MyUser)
class UserAdmin(admin.ModelAdmin):
	list_display = ['username', 'email', 'nickname']
	#fields = ('username', 'email','nickname', 'bio', 'profile_image', 'password', 'password2', 'first_name', 'last_name')
	form = UserRegisterForm