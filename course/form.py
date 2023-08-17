from django import forms
from .models import Student, Course

class AdmissionForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'})
    )
    phone = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'number'})
    )
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'address'})
    )
    city = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'})
    )
    state = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'state'})
    )
    zip_code = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'zip code'})
    )
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'date of birth'})
    )
    gender = forms.ChoiceField(
        choices=Student.GENDER_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
    )
    nationality = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nationality'})
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'date of birth'})
    )
    courses = forms.ModelMultipleChoiceField(
            queryset=Course.objects.all(),
            widget=forms.SelectMultiple(attrs={'class': 'form-control'})
        )




    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'date_of_birth', 'gender', 'nationality', 'image', 'courses']

