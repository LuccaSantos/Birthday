from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)    
    email = forms.EmailField(required=True)