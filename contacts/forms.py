from django import forms
from django.core.exceptions import ValidationError
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'notes']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Contact.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Contact with this Name already exists.")
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Contact with this Email already exists.")
        return email
