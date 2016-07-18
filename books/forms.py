from django import forms
from .models import Publisher,Contact,User
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError




class PublisherForm(ModelForm):
    class Meta:
        model=Publisher
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        fields = '__all__'

class RegistrationForm(ModelForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=20)),label=_("Password"))
    password2=forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True,max_length=20)),label=_("Confirm Password"))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2','date_of_birth','phone_number']

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("The two password didn't match."))
        return self.cleaned_data
    
            #if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
                #if self.cleaned_data['password1']!=self.cleaned_data['password2']:
                    #raise forms.ValidationError(_("The two password didn't match."))
            #return self.cleaned_data
            
        

