from django.shortcuts import render
from .models import Course
from .form import AdmissionForm

# Create your views here.
def index(request):
    course_list = Course.objects.all()
    return render(request, 'course/home.html', {'course_list': course_list})

def detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course/course.html', {'course': course})

def search(request):
    return render(request, 'course/search.html', {})

def about(request):
    return render(request, 'course/about.html', {})

def services(request):
    return render(request, 'course/services.html', {})

def contact(request):
    return render(request, 'course/contact.html', {})

def branches(request):
    return render(request, 'course/branches.html', {})

def admission(request):
    form = AdmissionForm()
    return render(request, 'course/admission.html', {'form': form})