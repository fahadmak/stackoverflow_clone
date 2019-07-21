from django.test import TestCase
from accounts.models import User


class TestQuestionModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            email="faga@gh.com",
            username="username",
            display_name="username",
            password="Philo1234")

    def test_title(self):
        user = User.objects.create(
            email="faga@gh.com",
            username="username",
            display_name="username",
            password="Philo1234")
        self.assertEquals(user.email, "faga@gh.com")
