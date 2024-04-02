from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

UserModel = get_user_model()


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_months = models.IntegerField(default=1)

    def __str__(self):
        return self.name


from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta


class UserSubscription(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user}'s Subscription"

    def calculate_duration(self):
        """
        Calculate the duration of the subscription in months.
        """
        return (self.end_date.year - self.start_date.year) * 12 + (self.end_date.month - self.start_date.month)
