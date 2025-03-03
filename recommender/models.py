from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Shoe(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[('daily_trainer', 'Daily Trainer'), ('race', 'Race'), ('trail', 'Trail'), ('stability', 'Stability')])
    weight = models.FloatField()  # in grams
    drop = models.FloatField()  # heel-to-toe drop in mm
    pronation = models.CharField(max_length=20, choices=[('neutral', 'Neutral'), ('stability', 'Stability')])
    cushioning = models.CharField(max_length=20, choices=[('minimalist', 'Minimalist'), ('max_cushion', 'Max Cushion'), ('energy_return', 'Energy Return')])
    terrain = models.CharField(max_length=20, choices=[('road', 'Road'), ('trail', 'Trail')])
    plate = models.BooleanField(default=False)  # Carbon plate?

    def __str__(self):
        return f"{self.brand.name} {self.model}"
