from django import forms
from mainapp.models import Mail


class SendMailForm(forms.ModelForm):
    
    class Meta:
        model = Mail
        fields = ['name', 'last_name', 'email', 'phone_number', 'text']
