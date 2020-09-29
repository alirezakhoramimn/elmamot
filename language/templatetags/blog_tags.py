from django import template 
from language.models import Post, Language, FrameWork
register = template.Library()
					
@register.simple_tag
def total_langs():
	return Language.objects.count()

@register.simple_tag
def total_frames():
	return FrameWork.objects.count()
"""
@register.simple_tag
def total_tags(request)
	return Post.objects.filter(
"""


