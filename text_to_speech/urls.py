from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', include('text_to_speech.profiles.urls')),
    path('', include('text_to_speech.web.urls')),
    path('audiofile/', include('text_to_speech.voices.urls')),
    path('accounts/', include('text_to_speech.accounts.urls')),
    path('subscriptions/', include('text_to_speech.subscriptions.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
