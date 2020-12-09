from rest_framework import status
from django.urls import reverse
from .models import Page, ContentAudio
from rest_framework.test import APITestCase

class GetAllPagesTest(APITestCase):
    def setUp(self):
        Page.objects.create(title='Casper')
        Page.objects.create(title='Muffin')
        Page.objects.create(title='Labrador')

    def test_page_list(self):
        response = self.client.get(reverse('page-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)


class GetSinglePageTest(APITestCase):
    """ Test module for GET single page API """
    def setUp(self):
        self.casper = Page.objects.create(title='Casper')
        self.ac = ContentAudio.objects.create(title='Kiss', bitrate=320)
        self.casper.contents.add(self.ac)

    def test_get_valid_single_page(self):
        response = self.client.get(reverse('page-detail', kwargs={'pk': self.casper.pk}))
        json = {"title":"Casper","contents":[{"textcontent":None,"videocontent":None,"audiocontent":{"id":2,"title":"Kiss","counter":0,"bitrate":320},"content_order":0}]}
        self.assertEqual(response.json(), json)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_page(self):
        response = self.client.get(reverse('page-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)