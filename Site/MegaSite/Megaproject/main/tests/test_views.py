from django.test import TestCase, Client
from django.urls import reverse
from main.models import Films, Genres
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('base')
        self.genrd_url = reverse('genrd', args=['rando'])
        self.genres1 = Genres.objects.create(
            slug='rando'
        )

        self.film_watch_url = reverse('film_watch', args=['5'])
        self.films1 = Films.objects.create(
            id=5,
            year='2003',
            img='dasldask.img',
            video='https://www.youtube.com/watch?v=TyHvyGVs42U&list=RDMM&index=9'
        )

    def test_project_base_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,  'main/base.html')

    def test_project_genrd_GET(self):
        response = self.client.get(self.genrd_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/genr.html')

    def test_project_film_watch_GET(self):
        response = self.client.get(self.film_watch_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/film_watch.html')



