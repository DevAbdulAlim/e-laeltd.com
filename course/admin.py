# admin.py
from django.contrib import admin
from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Batch,Instructor, Student, Service, Category, Branch
from django.utils.html import format_html

class BatchInline(admin.StackedInline):
    model = Batch
    extra = 0

class StudentInline(admin.TabularInline):
    model = Student.courses.through
    extra = 0



class CourseAdmin(admin.ModelAdmin):
    inlines = [BatchInline, StudentInline]
    list_display = ('name', 'price', 'total_student', 'is_active', 'start_date', 'end_date', 'duration_weeks', )

    def total_students(self, obj):
        return obj.total
    total_students.short_description = 'Students'






class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'instructor', 'capacity', 'is_active', 'created_at', 'updated_at',)
    search_fields = ('name', 'capacity', 'is_active', 'created_at', 'updated_at',)
    readonly_fields = ('is_full',)

class InstructorAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'full_name', 'email', 'phone_number', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'date_joined')
    # list_filter = ('batch_filter','course_filter')

    # def batch_filter(self, obj):
    #     return obj.batch__name
    
    # batch_filter.short_description = 'batch'
    
    # def course_filter(self, obj):
    #     return obj.course__name
    # course_filter.short_description = 'course'

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Name'

    def image_tag(self, obj):
        if obj.profile_picture:
            return format_html('<img src={} height="40 width="40" style="border-radius: 50%" />'.format(obj.profile_picture.url))
        else:
            return "Not Set"
    image_tag.short_description = "Photo"
        





class StudentAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'first_name', 'email', 'phone', 'date_of_birth', 'address')
    search_fields = ('first_name', 'courses__name', 'batches__name')
    list_per_page = 10
    list_filter = (('courses',admin.RelatedOnlyFieldListFilter), ('batches', admin.RelatedOnlyFieldListFilter))

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="40" width="40" style="border-radius: 50%" />'.format(obj.image.url))
        else:
            return "No Profile Pic"
    image_tag.short_description = 'Photo'

  

   

admin.site.register(Course, CourseAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(Branch)

admin.site.site_title = "Elearning"
admin.site.site_header = "e-laeltd Admin"
