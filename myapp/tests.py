from django.apps import apps
from django.test import TestCase
from django.urls import reverse


class MyAppViewTests(TestCase):
    def test_home_page_returns_success_and_expected_content(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, World!')
        self.assertContains(response, 'home page')

    def test_about_page_returns_success_and_expected_content(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Page')
        self.assertContains(response, 'about page')


class MyAppModelTests(TestCase):
    def test_app_config_is_registered(self):
        app_config = apps.get_app_config('myapp')

        self.assertEqual(app_config.name, 'myapp')

# add tests for your views and models here


