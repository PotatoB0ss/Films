from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import base, genr, film_watch


class TestUrls(SimpleTestCase):

    def test_base_url_resolves(self):
        url = reverse('base')
        self.assertEquals(resolve(url).func, base)

    def test_genr_url_resolves(self):
        url = reverse('genrd', args=['some-slug'])
        self.assertEquals(resolve(url).func, genr)              #Если тестируем класс то пишем .func.view_class

    def test_film_watch_url_resolves(self):
        url = reverse('film_watch', args=['2'])
        self.assertEquals(resolve(url).func, film_watch)

