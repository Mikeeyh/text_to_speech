from django.utils import timezone
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from text_to_speech.subscriptions.models import UserSubscription, SubscriptionPlan

UserModel = get_user_model()


class AudioFileCreateViewTests(TestCase):
    def test_get_create__when_logged_in_user__expect_200_and_correct_template(self):
        # Arrange
        user = UserModel.objects.create_user(email="test_user", password="1123QwER")
        self.client.login(email="test_user", password="1123QwER")

        # Act
        response = self.client.get(reverse("audiofile_create"))

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "voices/audiofile_create.html")
        self.assertEqual(user, response.context["user"])

    def test_get_create__when_anonymous_user__expect_302_with_redirect_to_login(self):
        # Arrange
        create_voice_url = reverse("audiofile_create")
        login_url = reverse("signin user")
        audio_data = {
            "text": "Mytestaudiotext",
            "title": "Mytestaudiotitle",
        }
        # Act
        response = self.client.post(
            create_voice_url,
            data=audio_data,
        )

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{login_url}?next={create_voice_url}"
        )

    def test_post_create__when_anonymous_user__expect_302_with_redirect_to_login(self):
        # Arrange
        create_voice_url = reverse("audiofile_create")
        login_url = reverse("signin user")
        audio_data = {
            "text": "Mytestaudiotext",
            "title": "Mytestaudiotitle",
        }
        # Act
        response = self.client.post(
            create_voice_url,
            data=audio_data,
        )

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            f"{login_url}?next={create_voice_url}"
        )

    def test_post_create__when_logged_in_user_without_subscription__expect_302_with_redirect_to_subscription_plans(self):
        # Arrange
        user = UserModel.objects.create_user(email="test_user", password="1123QwER")
        self.client.login(email="test_user", password="1123QwER")

        audio_data = {
            "text": "Mytestaudiotext",
            "title": "Mytestaudiotitle",
        }
        # Act
        response = self.client.post(
            reverse("audiofile_create"),
            data=audio_data,
        )

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse('view_plans', )
        )

    def test_post_create__when_logged_in_user_with_subscription__expect_302_with_correct_redirect_and_create_audio_file(self):
        # Arrange
        user = UserModel.objects.create_user(email="test_user", password="1123QwER")
        self.client.login(email="test_user", password="1123QwER")

        subscription_plan = SubscriptionPlan.objects.create(name="Test Plan", price=0)
        subscription_end_date = timezone.now() + timedelta(days=30)
        UserSubscription.objects.create(user=user, subscription_plan=subscription_plan, end_date=subscription_end_date)

        audio_data = {
            "text": "Mytestaudiotext",
            "title": "Mytestaudiotitle",
        }
        # Act
        response = self.client.post(
            reverse("audiofile_create"),
            data=audio_data,
        )

        # Assert
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse('audiofile-list', )
        )
