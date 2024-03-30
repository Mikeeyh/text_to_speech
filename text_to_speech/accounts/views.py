from django.shortcuts import redirect

from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy
from django.views import generic as views

from text_to_speech.accounts.forms import TextToVoiceUserCreationForm


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/signin_user.html"
    redirect_authenticated_user = True
    # This is to redirect to index page if user logged in but try to access login page from url


class SignUpUserView(views.CreateView):
    template_name = 'accounts/signup_user.html'
    form_class = TextToVoiceUserCreationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # 'form_valid' will call 'save'
        result = super().form_valid(form)

        login(self.request, form.instance)
        return result


def signout_user(request):
    logout(request)
    return redirect('index')
