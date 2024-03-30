from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse

from text_to_speech.core.view_mixins import OwnerRequiredMixin
from text_to_speech.profiles.forms import ProfileForm
from text_to_speech.profiles.models import Profile
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin

UserModel = get_user_model()
#
# def get_profile():
#     return Profile.objects.first()
#
#
# class DetailProfileView(views.DetailView):
#     template_name = "profiles/profile-details.html"
#
#     def get_object(self, queryset=None):
#         return get_profile()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['profile_exists'] = Profile.objects.exists()
#         context['user'] = self.request.user
#         return context
#
#
# class EditProfileView(views.UpdateView):
#     template_name = "profiles/profile-edit.html"
#     queryset = Profile.objects.all()
#     success_url = reverse_lazy("profile-detail")
#
#
# class DeleteProfileView(views.DeleteView):
#     template_name = "profiles/profile-delete.html"
#     success_url = reverse_lazy("index")
#
#     def get_object(self, queryset=None):
#         return get_profile()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['profile_exists'] = Profile.objects.exists()
#         context['user'] = self.request.user
#         return context


class ProfileDetailsView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DetailView):  # Add "OwnerRequiredMixin" if needed
    queryset = Profile.objects \
        .prefetch_related('user') \
        .all()

    # we add prefetch_related in order to show the user's email on profile details page without accessing the DB again

    template_name = "profiles/profile-details.html"


class ProfileUpdateView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.UpdateView):
    # queryset = Profile.objects.all()
    # template_name = "profiles/profile-edit.html"
    # fields = ("first_name", "last_name", "date_of_birth", "profile_picture")

    # OR USING FORM: (just remove get_form method and add get_object method if needed)
    model = UserModel
    form_class = ProfileForm
    template_name = "profiles/profile-edit.html"

    def get_success_url(self):
        return reverse("profile-detail", kwargs={"pk": self.object.pk})

    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #
    #     form.fields["date_of_birth"].widget.attrs["type"] = "date"
    #
    #     return form

    # ADD:
    def form_valid(self, form):
        # Ensure that the profile instance is correctly bound to the form data
        form.instance = self.get_object()
        return super().form_valid(form)

    # ADD:
    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.get_object()
        return kwargs


class ProfileDeleteView(views.DeleteView):
    # queryset = Profile.objects.all()
    model = Profile
    template_name = "profiles/profile-delete.html"
    success_url = reverse_lazy('index')

