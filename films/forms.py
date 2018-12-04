from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'name', 'email_address', 'subject', 'message'
        ]