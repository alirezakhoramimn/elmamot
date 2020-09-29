from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.views import generic
from account.models import Blogger
from .forms import QuestionFrameForm,QuestionLangForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class QuestionPostLangCreateView(generic.CreateView,LoginRequiredMixin):
	form_class = QuestionLangForm
	template_name = 'question/question_lang_create.html'

	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.user =blogger
		return super().form_valid(form)


class QuestionPostFrameCreateView(generic.CreateView,LoginRequiredMixin):
	form_class = QuestionFrameForm
	template_name = 'question/question_frame_create.html'

	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.user =blogger
		return super().form_valid(form)

class QuestionPostFrameUpdateView(generic.UpdateView,UserPassesTestMixin):
	form_class = QuestionFrameForm
	template_name = 'question/question_frame_update.html'

	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.user =blogger
		return super().form_valid(form)


	def test_func(self):
		post = self.get_object()
		if get_object_or_404(Blogger,user_blogger=self.request.user) == post.author:
			return True
		return False

class QuestionPostLangUpdateView(generic.UpdateView,UserPassesTestMixin):
	form_class = QuestionLangForm
	template_name = 'question/question_lang_update.html'

	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.user =blogger
		return super().form_valid(form)


	def test_func(self):
		post = self.get_object()
		if get_object_or_404(Blogger,user_blogger=self.request.user) == post.author:
			return True
		return False