from django.test import TestCase
from main.models import Films, Genres

class TestModels(TestCase):

    def setUp(self):
        self.film1 = Films.objects.create(
            title='omega'
        )