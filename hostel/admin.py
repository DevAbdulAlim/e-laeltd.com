from django.contrib import admin
from .models import Room, Booking, Payment

# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('get_room_number', 'guest', 'check_in_date', 'check_out_date', 'created_at',)

    def get_room_number(self, obj):
        return obj.room.room_number

    get_room_number.short_description = 'Room Number'


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'month', 'year', 'amount', 'payment_date', 'notes')

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)