from .models import Customer, Login, Course
from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password', widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')


class CustomerLogin(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ('user',)


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean(self):
        # data from the form is fetched using super function
        super(CourseForm, self).clean()

        # extract the name field from the data
        name = self.cleaned_data.get('name')

        # conditions to be met for the name length
        if len(name) < 5:
            self._errors['name'] = self.error_class([
                'Minimum 5 characters required'])

        # return any errors if found
        return self.cleaned_data
