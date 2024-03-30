from django.urls import path
from .views import view_plans, subscribe, subscription_success, subscription_detail, cancel_subscription, edit_subscription

urlpatterns = [
    path('subscribe/<int:plan_id>/', subscribe, name='subscribe'),
    path('subscription/success/', subscription_success, name='subscription_success'),
    path('subscription/detail/', subscription_detail, name='subscription_detail'),
    path('subscription/cancel/<int:subscription_id>/', cancel_subscription, name='cancel_subscription'),
    path('subscription/edit/<int:subscription_id>/', edit_subscription, name='edit_subscription'),
    path('plans/', view_plans, name='view_plans'),
]
