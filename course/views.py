from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Course, Category
from .form import AdmissionForm
from django.views import View
import json

# Create your views here.
def index(request):
    course_list = Course.objects.all()
    category_list = Category.objects.all()[:8]
    print(request.META)

    if request.META.get('CONTENT_TYPE') == 'application/json':
        json_course_list = serializers.serialize("json", course_list)
        return JsonResponse(json.loads(json_course_list), safe=False)

    else:    
        return render(request, 'course/home.html', {'course_list': course_list, 'category_list': category_list})


def detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course/course.html', {'course': course})

def categories(request):
    categories = Category.objects.all()
    return render(request, 'course/categories.html', {'categories': categories})

def about(request):
    return render(request, 'course/about.html', {})

def services(request):
    return render(request, 'course/services.html', {})

def contact(request):
    return render(request, 'course/contact.html', {})

def branches(request):
    return render(request, 'course/branches.html', {})


class AdmissionView(View):
    def get(self, request):
        form = AdmissionForm()
        return render(request, 'course/admission.html', {'form': form})