from django.contrib import admin
from .models import Employee, Salary, Expense

# Register your models here.
class salaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'amount', 'month', 'year', 'paid_date', )
    
    search_fields = ('employee', 'amount', 'month', 'year', 'paid_date')

    list_filter = ('employee', 'amount', 'month', 'year', 'paid_date')


admin.site.register(Employee)
admin.site.register(Salary, salaryAdmin)
admin.site.register(Expense)