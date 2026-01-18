#from django.contrib import admin
# Register your models here.


from django.contrib import admin
from .models import Pump, Nozzle, DailySale

@admin.register(Pump)
class PumpAdmin(admin.ModelAdmin):
    list_display = ['name', 'ownername', 'city']

# from .models import Nozzle
@admin.register(Nozzle)
class NozzleAdmin(admin.ModelAdmin):
    list_display = ['nozzle_number', 'pump', 'fuel_type', 'status']

@admin.register(DailySale)
class DailySaleAdmin(admin.ModelAdmin):
    list_display = ['nozzle', 'sale_date', 'liters_sold', 'total_amount']
    list_filter = ['sale_date', 'nozzle__fuel_type']
