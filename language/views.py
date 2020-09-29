
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
# GENERIC VIEWS
from django.views import generic
from django.views.generic.edit import UpdateView
# AUTHENTICATIONS
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# MDOELS
from .models import Language, FrameWork, Post
from account.models import Blogger
from taggit.models import Tag
# FORMS
from .forms  import  FrameCreateForm, LangCreateForm, CommentForm

# SEARCHING WITH POSTGRESQL
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank


# Create your views here.

# TESTED! PASSED
class LangCreateView(generic.edit.CreateView,LoginRequiredMixin):
	#model = Language

	form_class = LangCreateForm

	template_name = 'language/lang_create.html'
	queryset = Language.objects.all()

	 # adding the author to every post that is going to be created
	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.author =blogger
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('language:lang_detail',kwargs={'name':self.object.name, 'number':self.object.number})


class FrameCreateView(generic.edit.CreateView,LoginRequiredMixin):

	form_class = FrameCreateForm
	template_name = 'language/frame_create.html'

	queryset = FrameWork.objects.all()
	 # adding the author to every post that is going to be created
	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.author =blogger
		return super().form_valid(form)

	def get_success_url(self):
		return reverse('language:frame_detail',kwargs={'name':self.object.name,'lang':self.object.lang , 'number':self.object.number})

class FrameUpdateView(generic.edit.UpdateView,LoginRequiredMixin):

	form_class = FrameCreateForm
	fields = ['title','name' , 'number','lang', 'content', 'cat', 'summary']


	template_name = 'language/frame_update.html'

	 # adding the author to every post that is going to be created
	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.author =blogger
		return super().form_valid(form)


	def test_func(self):
		post = self.get_object()
		if get_object_or_404(Blogger,user_blogger=self.request.user) == post.author:
			return True
		return False



class LangUpdateView(generic.edit.UpdateView,LoginRequiredMixin):

	form_class = LangCreateForm
	fields = ['title','name' , 'number', 'content', 'cat', 'summary']
	model = Language
	template_name = 'language/lang_update.html'
	login_url = 'account:login'
	# adding the author to every post that is going to be created
	def form_valid(self, form):

		blogger = get_object_or_404(Blogger, user_blogger= self.request.user)
		form.instance.author = blogger
		return super().form_valid(form)



	def test_func(self):
		post = self.get_object()
		if get_object_or_404(Blogger,user_blogger=self.request.user) == post.author:
			return True
		return False




@login_required
def edit_lang_post(request,name,number):
	obj= get_object_or_404(Language, name=name, number=number)

	updater = Blogger(user_blogger = request.user)
	if request.method == 'POST':
		form = LangCreateForm(request.POST,instance=obj)
		if form.is_valid():

			form.save()

			messages.success(request, "You successfully updated the post")
			reverse('language:lang_detail',kwargs={'name':name, 'number':number})



		else:
			messages.error(request, 'شما نویسنده این مقاله نیستین!')
			form = LangCreateForm()

	else:
		form = LangCreateForm()

	context = {
		'form': form
	}
	return render(request, 'language/lang_update.html', context)




def home(request):

	langs = Language.objects.all()
	lang = Language.objects.filter(name='Python')
	f = []
	for l in lang:
		f.append(l.name)
	f = set(f)
	#color = COLORS[]

	return render(request, 'language/home.html',{'langs':langs, 'f':f})


COLORS = {
		'C-Sharp': '#8A2BE2',
		'HTML5' : '#D2691E',
		'Css3' : '#00BFFF',
		'C++' : '1E90FF',
		'git': '#F1502F',
		'GrapQL': '#e535ab',
		'Python':'#4B8BBE',
		'Js': '#f0db4f',
		'SQLServer' : '#be514b',
		'MySQL': '#F29111',
	    "PostgreSQL" : "#008bb9",
	    'linux' : '#E95420',
	    'docker': '#0db7ed',
	    'REST' : '#005442',
	    'Perl' : ' #eae0c8',
	    'Java' : '#f89820', 
	}

def frame_post_detail(request,lang,name,number):
	frames = FrameWork.objects.filter(name=name)

	framework_names = []
	frame_work_specific = []
	for frame in frames: 
		framework_names.append(frame.name)
		frame_work_specific.append(frame.filter(name=frame.name))

	framework_names = set(framework_names)
	

	frame_post = get_object_or_404(FrameWork, lang=lang, name=name, number=number)
	comments = frame_post.comments.filter(active=True)
	new_comment = None
	if request.method == 'POST':
		# get all the frameworks name
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid() and request.user.is_authenticated:

		# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign
			# the cur	rent post to the comment
			new_comment.post = frame_post
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = CommentForm()


	context = {
	'frames': frames,
	'langs' : langs,
	'framework_names' : framework_names,
	'frame_work_specific': frame_work_specific,
	'comments':comments,
	'new_comment':new_comment,
	'comment_form':comment_form,
	}

	return render(request, 'language/frame_detail.html', context)


def sidebar(request, name):

	context = {
	}
	return render(request, 'sidebar.html', context)


def lang_post_detail(request,name,number):

	lang_post = get_object_or_404(Language, name=name,number=number)
	color = COLORS[lang_post.name] 
	comments = lang_post.comments.filter(active=True)
	new_comment = None
	langs = Language.objects.filter(name=name)
	frames = FrameWork.objects.filter(lang=name)

	
	f_name = []

	for frame in frames:
		f_name.append(frame.name)
	f_name = set(f_name)

# Comment posted
	if request.method == 'POST':

		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid() and request.user.is_authenticated:

			# Create Comment object but don't save to database yet
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = lang_post
			new_comment.author = request.user
			# Save the comment to the database
			new_comment.save()
			messages.success(request,' با موفقیت ثبت گردید!')
		else:
			messages.error(request, 'خطایی رخ داده!')
			redirect('langauge:lang_post_detail')
	else:
		comment_form = CommentForm()

	context = {
		'langs': langs,
		'lang_post': lang_post,
		'comments':comments,
		'new_comment':new_comment,
		'comment_form':comment_form,
		'color':color,
		'f_name': f_name,

	}
	return render(request, 'language/lang_detail.html', context)


def post_search(request):
	query = request.GET.get('q')
	if query:
		search_vector = SearchVector('title', 'description')

		search_query = SearchQuery(query)

		results_lang = Language.objects.annotate(
		search=search_vector,
		rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')
		results_frame = FrameWork.objects.annotate(
			search=search_vector,
			rank=SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank')
	else:
		query = ''
		results_lang = ''
		results_frame = ''
	context = {
		'query': query,
		'results_lang': results_lang,
		'results_frame': results_frame,

	}


	return render(request,'language/search_results.html',context)



def all(request):
	langs = Post.objects.all().order_by('created')
	return render(request, 'language/all.html', {'langs':langs})