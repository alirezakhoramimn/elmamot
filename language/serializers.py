from rest_framework import serializers
from .models import FrameWork, Language



class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        exclude = ('is_framework', 'updated')


class FrameWorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FrameWork

        exclude = ('is_framework', 'updated')
