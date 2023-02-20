from django.forms import ModelForm
from .models import Room, Message
from django import forms

# Formuläret för användare att skapa rum


class Create_room_form(ModelForm):

    name = forms.CharField(
        label='Namn',
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
        })
    )
    description = forms.CharField(
        label='Beskrivning',
        widget=forms.Textarea(attrs={
            'autocomplete': 'off',
        })
    )

    class Meta:
        model = Room
        fields = ('name', 'description')
        required = False


# Formuläret för användare att skapa rum
class Create_message_form(ModelForm):
    message = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Skreiv Ett Meddelande...',
            'autocomplete': 'off',
        })
    )

    class Meta:
        model = Message
        fields = ('message', )
        required = False


# Formuläret för att söka efter rum

class search_room_form(forms.Form):
    name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Sök Efter Diskutioner',
            'autocomplete': 'off',
            'class': 'search'
        }))
