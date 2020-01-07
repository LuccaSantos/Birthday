from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):    
    class Meta:
        model = Friend
        fields = ('name', 'birthday', 'age', 'gift')

# class ClientDetailsForm(ModelForm):
    # birthday = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    # class Meta:
        # model = ClientDetails