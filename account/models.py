from django.db import models
from datetime import date
from calendar import month_name

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    total_salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.IntegerField(choices=[(i, month_name[i]) for i in range(1, 13)], default=date.today().month)
    year = models.IntegerField(choices=[(i, str(i)) for i in range(2000, date.today().year + 1)], default=date.today().year)
    paid_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ('employee', 'month', 'year')

    def __str__(self):
        return f"{self.employee} - {self.get_month_display()} {self.year}: ${self.amount}"

class Expense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField(default=date.today)
    category = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee} - ${self.amount} on {self.date}"

