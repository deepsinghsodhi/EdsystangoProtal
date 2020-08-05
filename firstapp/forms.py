from django import forms
from django.contrib.auth.models import User
from .models import FeeSubmission


class signup(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class FeeSubmitForm(forms.ModelForm):
    class Meta:
        model = FeeSubmission
        fields = '__all__'
        # widgets = {
        # 'FeeDate': DateInput(),
        # }
