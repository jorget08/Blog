from django import forms

from .models import Suscribers, Contact

class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        """Meta definition for Suscribersform."""

        model = Suscribers
        fields = ('email',)

        widgets = {
            'email': forms.EmailInput(attrs = {'placeholder': 'Ingresa email...'})
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('__all__')