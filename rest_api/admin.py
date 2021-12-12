from django.contrib import admin
from .models import Driver, Vehicle
# Register your models here.


@admin.register(Driver)
class AdminDriver(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name",
                    "created_at", "update_at")


@admin.register(Vehicle)
class AdminVehicle(admin.ModelAdmin):
    list_display = ("id", "driver_id", "model", "plate_number",
                    "created_at", "update_at")
