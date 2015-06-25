from django import forms
from water.models import Videos


class VideosForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ['url']