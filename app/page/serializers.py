from rest_framework import serializers
from .models import *


def create_content_serializer(model):
    return type('{}Serializer'.format(model.__name__),
                (serializers.ModelSerializer,),
                {'Meta': type('Meta', (), {'model': model, "fields": '__all__'})})


class PCS(serializers.ModelSerializer):

    textcontent = create_content_serializer(ContentText)(source='content.contenttext')
    videocontent = create_content_serializer(ContentVideo)(source='content.contentvideo')
    audiocontent = create_content_serializer(ContentAudio)(source='content.contentaudio')
    class Meta:
        model = PageContents
        fields = ['textcontent', 'videocontent', 'audiocontent', 'content_order',]


class PageSerializer(serializers.ModelSerializer):

    contents = PCS(source='pagecontents_set', many=True)

    class Meta:
        model = Page
        fields = ['title', "contents"]


class PageListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Page
        fields = ['url']