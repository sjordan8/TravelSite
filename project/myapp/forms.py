from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email",
            "password1", "password2")

    def save(self, commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __str__(self):
        return self.username

class TripForm(forms.Form):
    name = forms.CharField(label='Name', max_length=40)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    start_date = forms.DateField(label='Start Date', widget=forms.SelectDateWidget)
    end_date = forms.DateField(label='End Date', widget=forms.SelectDateWidget)
    image = forms.ImageField(label='Image')
    image_description = forms.CharField(label='Description', max_length=40)

class ProfileForm(forms.Form):
    city = forms.CharField(label='City', max_length=40)
    state = forms.CharField(label='State', max_length=40)
    country = forms.CharField(label='Country', max_length=40)
    email = forms.EmailField(label='Email')
