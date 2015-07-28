#from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.forms import ModelForm
from Letter.models import Letter
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':65}))

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = [
            'recipient', 'email', 'subject', 'text', 'date_received', 'privacy'
        ]




class LetterForm(forms.ModelForm):
    recipient = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':10, 'cols':65}))
    date_received = forms.SplitDateTimeField()
    # date_received = forms.DateTimeField(
    #     required=True,
    #     widget=DateTimePicker(options={"format": "YYYY-MM-DD HH:mm",
    #                                    "pickSeconds": False}))
    privacy = forms.BooleanField(required=False)

    class Meta:
        model = Letter
        exclude= ['date_created', 'author']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')