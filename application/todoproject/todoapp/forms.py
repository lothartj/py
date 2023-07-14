from django.forms import ModelForm
from .models import FormModel

class LoginForm(ModelForm):
    class Meta:
        model = FormModel
        fields = ['name','password']