from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _



class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('username','avatar')