from django.test import TestCase

from text_to_speech.subscriptions.models import SubscriptionPlan


class SubscriptionPlanModelTests(TestCase):
    def test_subscription_plan_upon_creation(self) -> None:
        subscription_plan = SubscriptionPlan.objects.create(
            name="TestSubscriptionPlan",
            price=10.5,
            duration_months=3,
        )

        created_test_subscription_plan = SubscriptionPlan.objects.get(pk=subscription_plan.pk)
        total_test_price_to_pay = created_test_subscription_plan.price * subscription_plan.duration_months

        self.assertEqual(created_test_subscription_plan.name, 'TestSubscriptionPlan')
        self.assertEqual(created_test_subscription_plan.price, 10.5)
        self.assertEqual(created_test_subscription_plan.duration_months, 3)
        self.assertEqual(31.5, total_test_price_to_pay)