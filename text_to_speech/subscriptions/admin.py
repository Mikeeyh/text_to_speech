from django.contrib import admin

from text_to_speech.subscriptions.models import SubscriptionPlan


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    exclude = ("duration_months",)
