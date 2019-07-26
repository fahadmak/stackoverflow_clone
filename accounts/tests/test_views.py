from django.test import TestCase
from django.urls import reverse
from questions.models import Question
from accounts.models import User


class TestUserView(TestCase):

    def test_login(self):
        self.credentials = {
            'display_name': 'testuser',
            'email': 'testuser',
            'username': 'testuser',
            'password': 'secret'}
        user = User.objects.create_user(**self.credentials)
        # send login data
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

        self.assertRedirects(response, reverse('questions:question_list'))

    def test_signup(self):
        self.credentials = {
            'email': 'testuser@gmail.com',
            'username': 'wacko123',
            'password1': 'secret1232',
            'password2': 'secret1232',
            }
        response = self.client.post('/accounts/signup/', self.credentials, follow=True)
        # should be signed up in now
        self.assertRedirects(response, reverse("accounts:login"))

    def test_logout(self):
        self.credentials = {
            'display_name': 'testuser',
            'email': 'testuser',
            'username': 'testuser',
            'password': 'secret'}
        user = User.objects.create_user(**self.credentials)
        # send login data
        self.client.post('/accounts/login/', self.credentials, follow=True)
        response2 = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response2.status_code, 302)
