from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from text_to_speech.voices.views import AudioFileCreateView, AudioFileDetailView, AudioFileUpdateView, \
    AudioFileDeleteView, AudioFileListView

urlpatterns = [
    path('create/', AudioFileCreateView.as_view(), name='audiofile_create'),
    path('<int:pk>/', AudioFileDetailView.as_view(), name='audiofile_detail'),
    path('<int:pk>/update/', AudioFileUpdateView.as_view(), name='audiofile_update'),
    path('<int:pk>/delete/', AudioFileDeleteView.as_view(), name='audiofile_delete'),

    path('audiofile/list/', AudioFileListView.as_view(), name='audiofile-list'),
]

# from django.conf import settings
# from django.conf.urls.static import static
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
