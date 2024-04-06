from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class SubscriptionPlansTests(TestCase):
    def test_view__subscription_plans__when_anonymous_user__expect_302_with_redirect_to_login(self):
        subscriptions_plans_url = reverse("audiofile_create")
        login_url = reverse("signin user")

        # Act
        response = self.client.get(subscriptions_plans_url)

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{login_url}?next={subscriptions_plans_url}"
        )

    def test_get_create__when_logged_in_user__expect_200_and_redirect_to_subscription_plans(self):
        # Arrange
        user = UserModel.objects.create_user(email="test_user", password="1123QwER")
        self.client.login(email="test_user", password="1123QwER")

        # Act
        response = self.client.get(reverse("view_plans"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "subscriptions/plans.html")
        self.assertEqual(user, response.context["user"])
