from django.utils import timezone
from dateutil.relativedelta import relativedelta

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SubscriptionPlan, UserSubscription


@login_required
def view_plans(request):
    plans = SubscriptionPlan.objects.all()
    user = request.user
    if user.is_authenticated:
        active_subscriptions = UserSubscription.objects.filter(user=user, end_date__gt=timezone.now())
        if active_subscriptions:
            return redirect('subscription_detail')
    return render(request, 'subscriptions/plans.html', {'plans': plans})


from django.urls import reverse


@login_required
def subscribe(request, plan_id):
    plan = SubscriptionPlan.objects.get(id=plan_id)
    user = request.user

    if UserSubscription.objects.filter(user=user, subscription_plan=plan, end_date__gt=timezone.now()).exists():
        messages.error(request, f"You are already subscribed to {plan.name}.")
        return redirect('view_plans')

    user_profile = user.profile

    duration = int(request.POST.get('duration', 1))

    total_price = plan.price * duration

    if user_profile.account_balance < total_price:
        messages.error(request, "Insufficient funds to subscribe to this plan.")
        return redirect('view_plans')

    user_profile.account_balance -= total_price
    user_profile.save()

    end_date = timezone.now() + relativedelta(months=duration)

    UserSubscription.objects.create(user=user, subscription_plan=plan, end_date=end_date)

    success_message = f"Successfully subscribed to {plan.name} for {duration} months."
    return redirect(reverse('subscription_success') + f'?success_message={success_message}')


@login_required
def subscription_success(request):
    success_message = request.GET.get('success_message')
    print("Success Message:", success_message)
    return render(request, 'subscriptions/subscription_success.html', {'success_message': success_message})


@login_required
def subscription_detail(request):
    user = request.user
    active_subscriptions = UserSubscription.objects.filter(user=user, end_date__gt=timezone.now())
    return render(request, 'subscriptions/subscription_detail.html', {'subscriptions': active_subscriptions})


@login_required
def cancel_subscription(request, subscription_id):
    subscription = get_object_or_404(UserSubscription, id=subscription_id)
    user = request.user

    if subscription.user != user:
        messages.error(request, "You do not have permission to cancel this subscription.")
        return redirect('subscription_detail')

    # Delete
    subscription.delete()

    messages.success(request, "Subscription canceled successfully.")
    return redirect('view_plans')


from django.utils import timezone
from django.contrib import messages


def edit_subscription(request, subscription_id):
    subscription = get_object_or_404(UserSubscription, id=subscription_id)
    user = request.user

    if subscription.user != user:
        messages.error(request, "You do not have permission to edit this subscription.")
        return redirect('subscription_detail')

    if request.method == 'POST':
        plan_id = request.POST.get('plan')
        if plan_id is None:
            messages.error(request, "Please select a subscription plan.")
            return redirect('subscription_detail')

        plan_id = int(plan_id)
        duration = int(request.POST.get('duration', 1))
        new_plan = get_object_or_404(SubscriptionPlan, id=plan_id)

        total_price_new = new_plan.price * duration
        total_price_old_per_month = subscription.subscription_plan.price / subscription.calculate_duration()
        total_price_new_per_month = total_price_new / duration

        if total_price_new_per_month <= total_price_old_per_month:
            messages.error(request, "The new subscription plan must have a higher total price per month than the current one.")
            return redirect('subscription_detail')

        if user.profile.account_balance < total_price_new:
            messages.error(request, "Insufficient funds to upgrade subscription.")
            return redirect('subscription_detail')

        user.profile.account_balance -= total_price_new
        user.profile.save()

        # Update subscription details
        new_end_date = subscription.end_date + relativedelta(months=duration)
        subscription.subscription_plan = new_plan
        subscription.end_date = new_end_date
        subscription.save()

        messages.success(request, f"Subscription updated to {new_plan.name} for {duration} months.")
        return redirect('subscription_detail')

    plans = SubscriptionPlan.objects.all()
    return render(request, 'subscriptions/subscription_edit.html', {'subscription': subscription, 'plans': plans})
