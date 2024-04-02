from django.conf import settings
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from gtts import gTTS
import os

from text_to_speech.core.view_mixins import OwnerRequiredMixin
from text_to_speech.profiles.models import Profile
from text_to_speech.subscriptions.models import UserSubscription
from text_to_speech.voices.forms import AudioFileForm
from text_to_speech.voices.models import AudioFile
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixin
from django.urls import reverse_lazy


# class AudioFileCreateView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.CreateView):
#     model = AudioFile
#     queryset = AudioFile.objects.all()
#     form_class = AudioFileForm
#     template_name = 'voices/audiofile_create.html'
#     success_url = reverse_lazy('audiofile-list')
#     context_object_name = 'audio_files'  # Define the context object name
#
#     def form_valid(self, form):
#         text = form.cleaned_data.get('text')
#         title = form.cleaned_data.get('title')
#
#         tts = gTTS(text)
#
#         directory_path = os.path.join(settings.MEDIA_ROOT, 'audio_files')
#         os.makedirs(directory_path, exist_ok=True)
#
#         filename = f'{title.replace(" ", "_")}.mp3'
#         filepath = os.path.join(directory_path, filename)
#
#         tts.save(filepath)
#
#         # form.instance.audio_file = filepath
#         # TEST:
#         form.instance.audio_file.name = os.path.relpath(filepath, settings.MEDIA_ROOT)
#
#         form.instance.user = self.request.user
#
#         # Save the form instance
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         audio_files = AudioFile.objects.filter(user=self.request.user)
#         print("Audio Files:", audio_files)  # Debug print
#         context[self.context_object_name] = audio_files
#         return context

import requests

CHUNK_SIZE = 1024  # Size of chunks to read/write at a time
XI_API_KEY = "2313a1fbc5eebdb4ec07393226cf81be"  # API key
VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # ID VOICE


class AudioFileCreateView(auth_mixin.LoginRequiredMixin, views.CreateView):
    model = AudioFile
    form_class = AudioFileForm
    template_name = 'voices/audiofile_create.html'
    success_url = reverse_lazy('audiofile-list')
    context_object_name = 'audio_files'

    def form_valid(self, form):
        if not self.has_subscription():
            messages.warning(self.request, "Please subscribe to a plan to create audio files.")
            return redirect('view_plans')

        text = form.cleaned_data.get('text')
        title = form.cleaned_data.get('title')

        # Construct the URL for the Text-to-Speech API request
        tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/stream"

        # Set up headers for the API request, including the API key for authentication
        headers = {
            "Accept": "application/json",
            "xi-api-key": XI_API_KEY
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.8,
                "style": 0.0,
                "use_speaker_boost": True
            }
        }

        # Make the POST request to the TTS API with headers and data, enabling streaming response
        response = requests.post(tts_url, headers=headers, json=data, stream=True)

        # Check if the request was successful
        if response.ok:
            # Save synthesized audio as an MP3 file
            directory_path = os.path.join(settings.MEDIA_ROOT, 'audio_files')
            os.makedirs(directory_path, exist_ok=True)
            filename = f'{title.replace(" ", "_")}.mp3'
            filepath = os.path.join(directory_path, filename)
            with open(filepath, 'wb') as f:
                # Read the response in chunks and write to the file
                for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)

            # Save the form instance
            form.instance.audio_file.name = os.path.relpath(filepath, settings.MEDIA_ROOT)
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            # Print the error message if the request was not successful
            print(response.text)
            return super().form_invalid(form)

    def has_subscription(self):
        # Check if the user has an active subscription
        user = self.request.user
        active_subscriptions = UserSubscription.objects.filter(user=user, end_date__gt=timezone.now()).exists()
        return active_subscriptions


class AudioFileDetailView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DetailView):
    # model = AudioFile
    queryset = AudioFile.objects.all()
    template_name = 'voices/audiofile_details.html'
    context_object_name = 'audio_file'


class AudioFileListView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.ListView):
    model = AudioFile
    template_name = 'voices/audiofile_list.html'
    context_object_name = 'audio_files'

    def get_queryset(self): # added
        return AudioFile.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_audio_files'] = self.get_queryset().count()
        return context


class AudioFileUpdateView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.UpdateView):
    model = AudioFile
    fields = ['title']
    template_name = 'voices/audiofile_edit.html'  # Change this to your desired template name
    # success_url = reverse_lazy('audiofile-list')  # Change this to your actual URL name for audio file list view

    def get_success_url(self):
        return reverse("audiofile_detail", kwargs={"pk": self.object.pk})


class AudioFileDeleteView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = AudioFile
    template_name = 'voices/audiofile_delete.html'
    success_url = reverse_lazy('audiofile-list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
