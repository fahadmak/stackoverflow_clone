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

    def test_super_user_created(self):
        user = User.objects.create_superuser(
            email="faga@gh.com",
            username="username",
            display_name="username",
            password="Philo1234")

        self.assertEquals(user.display_name, "username")

    def test__user_created(self):
        user = User.objects.create_user(
            email="faga@gh.com",
            username="username",
            display_name="username",
            password="Philo1234")

        self.assertEquals(user.display_name, "username")
        self.assertEquals(user.get_short_name(), "username")
        self.assertEquals(user.get_long_name(), "username @(username)")
        self.assertEquals(str(user), "@username")
