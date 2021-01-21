from django.forms import ModelForm
from .models import UsersAll

class Reviewform(ModelForm):
    class Meta:
        model = UsersAll
        fields = ['review']