from django.shortcuts import render
from text_to_speech.profiles.models import Profile


def index(request):
    if request.user.is_authenticated:
        template_name = 'web/home-with-profile.html'
    else:
        template_name = 'base.html'

    context = {
        'user': request.user,
    }

    return render(request, template_name, context)


# # views.py
import os
from django.conf import settings
from django.http import HttpResponse, Http404


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="audio/mpeg")
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404


from django.shortcuts import render, redirect
from django.contrib import messages
from decimal import Decimal


def add_money(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            try:
                amount = Decimal(amount)
            except ValueError:
                messages.error(request, "Invalid amount. Please enter a valid number.")
                return redirect('add_money')

            if amount <= 0:
                messages.error(request, "Amount must be greater than zero.")
                return redirect('add_money')

            user_profile = Profile.objects.get(user=request.user)
            user_profile.account_balance += amount  # Adding a Decimal object to another Decimal object
            user_profile.save()

            messages.success(request, f"Successfully added {amount} to your account balance.")
            return redirect('view_plans')
        else:
            messages.error(request, "Amount cannot be empty.")
            return redirect('add_money')
    else:
        return render(request, 'web/add_money.html')
