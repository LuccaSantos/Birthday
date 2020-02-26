from django import forms
from .models import Friend


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ('name', 'birthday', 'age', 'gift')


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(required=True)


