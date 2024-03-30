# from django import forms
#
# from Speechify.voices.models import AudioFile
#
#
# class AudioFileForm(forms.ModelForm):
#     class Meta:
#         model = AudioFile
#         fields = ['title', 'text']

from django import forms

from text_to_speech.voices.models import AudioFile


class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['title', 'text']
        labels = {
            'title': 'Title',
            'text': 'Text'
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50})
        }

