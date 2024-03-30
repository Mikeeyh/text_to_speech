# from django.urls import path
#
# from Text_to_Voice.profiles.views import DetailProfileView, DeleteProfileView, EditProfileView
#
# urlpatterns = (
#     path('details/', DetailProfileView.as_view(), name='profile-detail'),
#     path("delete/", DeleteProfileView.as_view(), name="delete_profile"),
#     path("edit/", EditProfileView.as_view(), name="edit_profile"),
# )

from django.urls import path, include

from text_to_speech.profiles.views import ProfileDetailsView, ProfileUpdateView, ProfileDeleteView

urlpatterns = (
    path(
        "profile/<int:pk>/", include([
            path('details/', ProfileDetailsView.as_view(), name='profile-detail'),
            path("delete/", ProfileDeleteView.as_view(), name="delete-profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit-profile"),
        ])
    ),
)
