from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name', 'name', 'email_address', 'subject', 'message'
        ]
        widgets = {
            'message': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}),
        }