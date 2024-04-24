# to test URL

# from django.test import TestCase

from django.test import TestCase
from django.urls import resolve, reverse
from shopee.views import *




#
# class TestURL(TestCase):
#     def test_home(self):
#         result=self.client.get('/')
#         print(result)
#         self.assertEqual(result.status_code, 200)






# reverse and resolve met hod

from django.test import TestCase
from django.urls import resolve, reverse
from shopee.views import *

class TestUrl(TestCase):
    def test_home(self):
        url=reverse('home')
        print('url is', url)
        self.assertEqual(resolve(url).func, home)
        self.assertTemplateUsed('home.html')
        print(resolve(url))



#





