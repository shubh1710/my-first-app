from django import forms
from .models import Publisher,Contact
from django.forms import ModelForm

class PublisherForm(ModelForm):
    class Meta:
        model=Publisher
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields = '__all__'
        

