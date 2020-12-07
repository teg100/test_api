import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .serializers import *
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
client = Client()

class GetAllPagesTest(TestCase):
    def setUp(self):
        Page.objects.create(title='Casper')
        Page.objects.create(title='Muffin')
        Page.objects.create(title='Labrador')

    def test_page_list(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('page-list'))
        response = client.get(reverse('page-list'))
        pages = Page.objects.all()
        serializer = PageListSerializer(pages, many=True, context={'request': Request(request)})
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSinglePuppyTest(TestCase):
    """ Test module for GET single puppy API """
    def setUp(self):
        self.casper = Page.objects.create(title='Casper')
        self.ac = ContentAudio.objects.create(title='Kiss', bitrate=320)
        self.tc = ContentText.objects.create(title='Article', text='Lorem')
        self.vc = ContentVideo.objects.create(title='Youtube', video_url='https://localhost.com',
                                              subtitle_url="https://localhost.com")
        self.casper.contents.add(self.ac)

    def test_get_valid_single_page(self):
        response = client.get(reverse('page-detail', kwargs={'pk': self.casper.pk}))
        page = Page.objects.get(pk=self.casper.pk)
        serializer = PageSerializer(page)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_page(self):
        response = client.get(reverse('page-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)