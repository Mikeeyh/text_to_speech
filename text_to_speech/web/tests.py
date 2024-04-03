from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class IndexFbvTests(TestCase):
    def test_index__with_no_user_authenticated__returns_base_html(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "base.html")
        self.assertEqual(200, response.status_code)

    def test_index__when_a_user_is_authenticated__returns_home_with_profile_html(self):
        # Arrange
        user = UserModel.objects.create_user(email="test_user", password="1123QwER")

        self.client.login(email="test_user", password="1123QwER")
        # Act
        response = self.client.get(reverse("index"))

        # Assert
        self.assertTemplateUsed(response, "web/home-with-profile.html")
        self.assertEqual(200, response.status_code)
        self.assertIn("user", response.context)
        self.assertEqual(user, response.context["user"])

