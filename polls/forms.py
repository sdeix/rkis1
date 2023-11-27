from django.contrib.auth.forms import UserCreationForm
from .models import User, Question, Choice
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('username','avatar')


class AddForm(forms.ModelForm):
    img = forms.ImageField(label="Pic an avatar",
                              required=False)

    question_text = forms.CharField(label='Вопрос', widget=forms.TextInput, required=True)
    description = forms.CharField(label='Описание', widget=forms.TextInput, required=True)
    num_of_questions = forms.IntegerField(label='Количество вариантов', required=True)

    def clean_num_of_questions(self):
        cd = self.cleaned_data
        if cd['num_of_questions'] < 2 or cd['num_of_questions'] > 10:
            raise forms.ValidationError('Число вариантов не может быть меньше 2 а также больше 10')
        return cd['num_of_questions']

    def clean_img(self):
        cd = self.cleaned_data
        return cd['img']
    class Meta:
        model = Question
        fields = ['img', 'question_text', 'description', 'num_of_questions']

class AddFormchoice(forms.ModelForm):
    choice_text = forms.CharField(label='Вопрос', widget=forms.TextInput, required=True)

    def clean_choice_text(self):
        cd = self.cleaned_data
        if not cd['choice_text']:
            raise forms.ValidationError('Поле обязательно для заполнения')
        return cd['choice_text']

    class Meta:
        model = Choice
        fields = ['choice_text']