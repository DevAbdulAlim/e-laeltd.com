from django.db import models
# from django.contrib.auth.models import User
from course.models import Student
from datetime import date
from calendar import month_name

# Create your models here.
class Room(models.Model):
    ROOM_TYPE_CHOICES = (
    ('single', 'Single'),
    ('double', 'Double'),
    ('twin', 'Twin'),
    ('triple', 'Triple'),
    ('quad', 'Quad'),
    ('suite', 'Suite'),
)
    room_number = models.CharField(max_length=20)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPE_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.room_numbers

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(Student, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.room.room_number}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.Case)
    month = models.IntegerField(choices=[(i, month_name[i]) for i in range(1, 13)], default=date.today().month)
    year = models.IntegerField(choices=[(i, str(i)) for i in range(2000, date.today().year + 1)], default=date.today().year)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateField(auto_now_add = True)
    notes = models.TextField(blank=True)
    