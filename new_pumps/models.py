from django.db import models

class Pump(models.Model):
    name = models.CharField(max_length=100)
    ownername = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Nozzle(models.Model):
    FUEL_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
    ]
    pump = models.ForeignKey(Pump, on_delete=models.CASCADE)
    nozzle_number = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=10, choices=FUEL_TYPES)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.pump.name} Nozzle {self.nozzle_number} ({self.fuel_type})"

class DailySale(models.Model):
    nozzle = models.ForeignKey(Nozzle, on_delete=models.CASCADE)
    sale_date = models.DateField(auto_now_add=True)
    liters_sold = models.DecimalField(max_digits=8, decimal_places=2)
    rate_per_liter = models.DecimalField(max_digits=8, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_amount = self.liters_sold * self.rate_per_liter
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nozzle} - {self.liters_sold}L @ ₹{self.rate_per_liter} = ₹{self.total_amount}"
