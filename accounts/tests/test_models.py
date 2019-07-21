from django.test import TestCase
from accounts.models import User


class TestUserModel(TestCase):

    def test_title(self):
        user = User.objects.create(
            email="faga@gh.com",
            username="username",
            display_name="username",
            bio="bio",
            is_active=True,
            password="Philo1234")
        self.assertEquals(user.email, "faga@gh.com")
        self.assertEquals(user.bio, "bio")
