from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

class PageTestCase(TestCase):
    def test_display_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_display_registration(self):
        User.objects.filter()
        response = self.client.get(reverse("registration"))
        self.assertEqual(response.status_code, 200)

    def test_register_user(self):
        username = "franta"
        password = "1234franta56789"
        
        self.assertFalse(User.objects.filter(username=username).exists())
        
        response = self.client.post(
            reverse("registration"),
            {
                "username": "franta",
                "password1": password,
                "password2": password,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))
        self.assertTrue(User.objects.filter(username=username).exists())