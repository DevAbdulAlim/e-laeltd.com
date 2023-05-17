from django import forms
from .models import Student

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip_code', 'date_of_birth', 'gender', 'nationality', 'image', 'courses']

