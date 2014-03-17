from django.test import TestCase
from projects.models import Project
from projects.views import index
# Create your tests here.


class IndexTest(TestCase):
    def test_call_view_denies_anonymous(self):
        response = self.client.get('', follow=True)
        self.assertRedirects(response, '/users/login/')
        response = self.client.post('', follow=True)
        self.assertRedirects(response, 'users/login/')
