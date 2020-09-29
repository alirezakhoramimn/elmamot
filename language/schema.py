from graphene_django import DjangoObjectType 
from .models import Language, FrameWork, Comment
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
			return queryset.exlude('author')
		return queryset



class FrameWorkType(DjangoObjectType):
	class Meta:
		model = FrameWork

	@classmethod
	def get_queryset(cls, queryset, info):
		if info.context.user.is_anonymous:
			return queryset.exlude('author')
		return queryset



class CommentType(DjangoObjectType):
	class Meta:
		model = Comment
		exclude = ('author',)

class Query(graphene.ObjectType):
	
	framework = graphene.List(FrameWorkType)


	language = graphene.List(LanguageType)
	
	framework_by_number = graphene.Field(FrameWorkType, number=graphene.Int())

	language_by_number = graphene.Field(FrameWorkType, number=graphene.Int())

	framework_by_topic = graphene.Field(FrameWorkType, name =graphene.String())


	language_by_topic= graphene.Field(FrameWorkType,  name =graphene.String())

	comment = graphene.List(CommentType)

	comment_by_topic = graphene.Field(CommentType, name=graphene.String(), number = graphene.Int(), is_framework = graphene.Boolean())
	language_specific = graphene.Field(LanguageType, name=graphene.String(), number = graphene.Int())
	framework_specific = graphene.Field(FrameWorkType, name=graphene.String(), number = graphene.Int())

	def resolve_framework(root, info, **kwargs):
		# Return All of the FrameWorks 
		# Querying a list
		return FrameWork.objects.all()


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

	def resolve_language_specific(root, info, name, number):
		return get_object_or_404(Language, name=name, number=number)

	def resolve_framework_specific(root, info, name, number):
		return get_object_or_404(Language, lang=name, number=number)


	def resolve_comment(root, info, **kwargs):
		return Comment.objects.all()
'''
	def resolve_comment_by_post(root, info, name, number, is_framework):
		if is_framework:
			frame =  get_object_or_404(FrameWork, lang=name, number = number)
			return
		else:
			return get_list_or_404(Language, name=name, number=number)
'''
class Mutation(graphene.ObjectType):
	pass
