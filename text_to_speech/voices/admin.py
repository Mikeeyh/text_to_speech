from django.contrib import admin

from text_to_speech.voices.models import AudioFile


@admin.register(AudioFile)
class AudioFileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'created_at')
