# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
#
# from text_to_speech.subscriptions.models import SubscriptionPlan
#
# UserModel = get_user_model()
#
#
# class SubscriptionPlanModelTests(TestCase):
#     def test_subscription_plan_upon_creation(self) -> None:
#         subscription_plan = SubscriptionPlan.objects.create(
#             name="TestSubscriptionPlan",
#             price=10.5,
#             duration_months=3,
#         )
#
#         created_test_subscription_plan = SubscriptionPlan.objects.get(pk=subscription_plan.pk)
#         total_test_price_to_pay = created_test_subscription_plan.price * subscription_plan.duration_months
#
#         self.assertEqual(created_test_subscription_plan.name, 'TestSubscriptionPlan')
#         self.assertEqual(created_test_subscription_plan.price, 10.5)
#         self.assertEqual(created_test_subscription_plan.duration_months, 3)
#         self.assertEqual(31.5, total_test_price_to_pay)
#
#
# class SubscriptionPlansTests(TestCase):
#     def test_view__subscription_plans__when_anonymous_user__expect_302_with_redirect_to_login(self):
#         subscriptions_plans_url = reverse("audiofile_create")
#         login_url = reverse("signin user")
#
#         # Act
#         response = self.client.get(subscriptions_plans_url)
#
#         # Assert
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(
#             response,
#             f"{login_url}?next={subscriptions_plans_url}"
#         )
#
#     def test_get_create__when_logged_in_user__expect_200_and_redirect_to_subscription_plans(self):
#         # Arrange
#         user = UserModel.objects.create_user(email="test_user", password="1123QwER")
#         self.client.login(email="test_user", password="1123QwER")
#
#         # Act
#         response = self.client.get(reverse("view_plans"))
#
#         # Assert
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, "subscriptions/plans.html")
#         self.assertEqual(user, response.context["user"])
