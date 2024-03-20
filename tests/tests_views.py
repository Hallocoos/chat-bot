from django.test import TestCase
from django.urls import reverse

class MyViewTests(TestCase):
    def test_my_view(self):
        response = self.client.get(reverse('my_view_url'))
        self.assertEqual(response.status_code, 200)