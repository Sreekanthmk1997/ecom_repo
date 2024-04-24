from django.test import TestCase
from shopee.models import *
class TestModels(TestCase):
    def tast_category(self):
        category1=Category.objects.create(name='Home and Living', slug='home', desc='demo')
        self.assertEqual(str(category1), 'Home and Living')
        self.assertTrue(isinstance(category1, Category))
