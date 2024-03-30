from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('Speechify.profiles.urls')),
    path('', include('Speechify.web.urls')),
    path('audiofile/', include('Speechify.voices.urls')),
    path('accounts/', include('Speechify.accounts.urls')),
]
sdsad