# RENDERING
from django.shortcuts import render,redirect,get_object_or_404
# ROUTING
from django.urls import reverse_lazy, reverse
# MODELS
from .models import Student, Blogger, MyUser
from language.models import FrameWork, Language
# GENERIC VIEWS
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView,FormView, RedirectView
from django.views import generic
from django.views.generic.base import TemplateResponseMixin
from django.conf import settings
# FORMS
from .forms import  UserRegisterForm,BloggerRegisterationForm, UserLoginForm
# MIXINS
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# AUTH
from django.contrib.auth.decorators import login_required
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters



@csrf_protect
@login_required()
def profile_student(request,username):
	if request.method == 'POST':
		#lang = Language.objects.filter()
		user_student = get_object_or_404(MyUser, username=username)

	else:
		user_student=''
	context = {
	'user_student':user_student
	}
	return render(request,'registration/profile_student.html', context)


class StudentProfileView(DetailView):
	model = Student
	template_name = 'registration/profile_student.html'
	
	def get_object(self, queryset=None):
		return get_object_or_404(Student, user_student__username=self.kwargs['username'])

class BloggerProfileView(generic.TemplateView):
	model = Blogger
	template_name='registration/profile_blogger.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		# add categories for navbar link texts
		who_is_user = get_object_or_404(Blogger, user_blogger__username=self.kwargs['username'])
		
		context['blogger'] = who_is_user
		context['langs'] = langs = get_object_or_404(Language, author=who_is_user)
		context['frames'] = get_object_or_404(FrameWork,author=who_is_user)

		return context

@csrf_protect
def profile_blogger(request, username):

	myuser = get_object_or_404(MyUser,username=username)
	blogger = get_object_or_404(Blogger,user_blogger=myuser)
	langs = get_object_or_404(Language, author=blogger)
	frames = get_object_or_404(FrameWork,author=blogger)

	if langs:
		pass
	else:
		langs = 'این خوشگل پسر هنوز هیچی نزاشته !'
	
	
	if frames: 
		pass
	else:
		frames = 'ین خوشگل پسر هنوز هیچی نزاشته'

	context = {
		'langs':langs,
		'frames':frames,
		'blogger':blogger
	}

	return render(request, 'registration/profile_blogger.html', context)
#


'''
class UserPostListView(generic.ListView):
	model = Post
	template_name = 'blog/profile_blogger.html'
	# let's set the context in here as well
	context_object_name = 'posts'
	# now for having the latest post we add the ordering
	paginate_by = 5

	# we can overwirte a method and change the queryset
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		blogger = get_object_or_404(Blogger, user=user)
		return Post.objects.filter(author=user).order_by('created_on')
'''



class SignUp(CreateView):
	form_class = UserRegisterForm
	template_name = 'registration/signup2.html'


	def from_valid(self, form):
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('account:login')

class LoginView(FormView):
	form_class = UserLoginForm
	template_name = 'registration/login.html'

	#@method_decorator(csrf_protect)
	#@method_decorator(never_cache)
	def form_valid(self, form):
		if self.request.user.is_authenticated:
			if self.request.user.blogger_or_student == 'blogger':
				return redirect('account:profile_blogger', kwargs={'username':self.request.user.username})
			elif self.request.user.blogger_or_student == 'student':
				return redirect('account:profile_student', kwargs={'username':self.request.user.username})

		else:
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(	
								request=self.request, 
								username=username, 
								password=password)

			if user is not None and user.is_active:
				auth_login(self.request, user)
				
				return super(LoginView, self).form_valid(form)
			else:
				return self.form_invalid(form)
			
		return super(LoginView, self).form_valid(form)

		
	def get_success_url(self):
		if self.request.user.blogger_or_student == 'blogger':
			return reverse('account:profile_blogger' ,kwargs={'username':self.request.user.username})
		elif self.request.user.blogger_or_student == 'student':
			return reverse('account:profile_student', kwargs={'username':self.request.user.username})

		

class LogoutView(RedirectView):
	"""
	Provides users the ability to logout
	"""
	url = '/account/login/'
	
	template_name = 'registration/logout.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:

			auth_logout(request)
			redirect('language:home')
		else:

			messages.error(request, 'شما که اصلا لاگین نکردی')
		
		return super(LogoutView, self).get(request, *args, **kwargs)
		

















def home(request):
	return redirect('langauage:home')











class StudentTasksViewPublic(ListView):
	'''
	The context_object_name attribute on a generic view specifies the context variable to use
	'''
	'''
	Another common need is filtering, if we wanted, we could use
		def get_queryset(self):
			user = self.request.user
			if user.is_authenticated:
				return Contact.objects.filter(created_by=self.request.user)
			return Contact.objects.filter(created_by=None)

	'''
	pass



class PersonEditProfileView(LoginRequiredMixin):
	pass


class StudentLoginView():
	pass
class StudentRegisterView:
	pass


class BloggerRegisterView:
	pass



class BloggerLoginView:
	pass


class BloggerDeleteView:
	pass


class BloggerResetPasswordView:
	pass

class BloggerEditProfileView:
	pass
