from graphene_django import DjangoObjectType 
from .models import Language, FrameWork, CommentLanguage, CommentFrameWork
import graphene 
from django.shortcuts import get_object_or_404, get_list_or_404
import graphene




class LanguageType(DjangoObjectType):
	class Meta:
		model = Language
		exlude = ('is_framework',)

	@classmethod
	def get_queryset(cls, queryset, info):
		if info.context.user.is_anonymous:
			return queryset.exlude('author__user_blogger__password')
		return queryset



class FrameWorkType(DjangoObjectType):
	class Meta:
		model = FrameWork

	@classmethod
	def get_queryset(cls, queryset, info):
		if info.context.user.is_anonymous:
			return queryset.exlude('author__user_blogger__password')
		return queryset



class CommentLanugageType(DjangoObjectType):
	class Meta:
		model = CommentLanguage
		exclude = ('author__password',)



class CommentFrameWorkType(DjangoObjectType):
	class Meta:
		model = CommentFrameWork
		exclude = ('author__password',)


class Query(graphene.ObjectType):
	
	framework = graphene.List(FrameWorkType)


	language = graphene.List(LanguageType)
	
	framework_by_number = graphene.Field(FrameWorkType, number=graphene.Int())

	language_by_number = graphene.Field(FrameWorkType, number=graphene.Int())

	framework_by_topic = graphene.Field(FrameWorkType, name =graphene.String())


	language_by_topic= graphene.Field(FrameWorkType,  name =graphene.String())

	comment_language = graphene.List(CommentLanugageType)

	comment_framework = graphene.List(CommentFrameWorkType)

	comment_language_by_topic = graphene.Field(CommentLanugageType, name=graphene.String(), number = graphene.Int())
	
	comment_framework_by_topic = graphene.Field(CommentFrameWorkType, name=graphene.String(), number = graphene.Int())

	language_specific = graphene.Field(LanguageType, name=graphene.String(), number = graphene.Int())

	framework_specific = graphene.Field(FrameWorkType, name=graphene.String(), number = graphene.Int())

	# passed
	def resolve_framework(root, info, **kwargs):
		# Return All of the FrameWorks 
		# Querying a list
		return FrameWork.objects.all()

	# passed
	def resolve_language(root, info, **kwargs):
		# Return All of the FrameWorks 
		# Querying a list
		return Language.objects.all()

	def resolve_language_by_number(root, info, number):
		return get_list_or_404(Language, number=number)

	def resolve_framework_by_number(root, info, number):
		return get_list_or_404(FrameWork, number=number)
	

	def resolve_language_by_topic(root, info, name):
		return get_list_or_404(Language, name=name)

	def resolve_framework_by_topic(root, info, name):
		return get_list_or_404(FrameWork, lang=name)

	# passed

	def resolve_language_specific(root, info, name, number):
		return get_object_or_404(Language, name=name, number=number)
	# passed

	def resolve_framework_specific(root, info, name, number):
		return get_object_or_404(FrameWork, lang=name, number=number)


	def resolve_language_comment(root, info, **kwargs):
		return CommentLanguage.objects.all()

	def resolve_framework_comment(root, info, **kwargs):
		return CommentFrameWork.objects.all()

	def resolve_comment_language_by_topic(root, info, name, number):

		return CommentLanguage.objects.filter(name=name, number=number)

	def resolve_comment_framework_by_topic(root, info, name, number):

		return CommentFrameWork.objects.filter(lang=name, number=number)


'''
	def resolve_comment_by_post(root, info, name, number, is_framework):
		if is_framework:
			frame =  get_object_or_404(FrameWork, lang=name, number = number)
			return
		else:
			return get_list_or_404(Language, name=name, number=number)
'''

class CreateLanguageComment(graphene.Mutation):
	comment_language = graphene.List(CommentLanugageType)

	class Arguments:
		name_of_topic_of_post = graphene.String()
		number_of_post = graphene.Int()
		body = graphene.String()

	def mutate(self, info, **kwargs):
		name = kwargs.get('name_of_topic_of_post')
		number = kwargs.get('number_of_post')
		body = kwargs.get('body')

		language = get_object_or_404(Language, name=name, number=number)
 # context will reference to the Django request
		if not info.context.user.is_authenticated:

			created_comment = CommentLanguage.objects.create(post=language, body=body,author=info.context.user)

			return CreateLanguageComment(comment_language=created_comment)
		else:
			return CommentLanguage.objects.none()


class CreateFrameWorkComment(graphene.Mutation):
	comment_framework = graphene.List(CommentFrameWorkType)

	class Arguments:
		name_of_topic_of_post = graphene.String()
		number_of_post = graphene.Int()
		body = graphene.String()

	def mutate(self, info, **kwargs):
		name = kwargs.get('name_of_topic_of_post')
		number = kwargs.get('number_of_post')
		body = kwargs.get('body')

		framework = get_object_or_404(FrameWork, name=name, number=number)
 # context will reference to the Django request
		if not info.context.user.is_authenticated:

			created_comment = CommentFrameWork.objects.create(post=framework, body=body,author=info.context.user)

			return CreateFrameWorkComment(comment_language=created_comment)
		else:
			return CommentFrameWork.objects.none()




class Mutation(graphene.ObjectType):
	create_comment_language = CreateLanguageComment.Field()
	create_comment_framework = CreateFrameWorkComment.Field()