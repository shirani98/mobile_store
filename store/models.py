from django.db import models


class Mobile(models.Model):
    model = models.CharField(max_length=100, unique=True)
    brand_name = models.CharField(max_length=100)
    country_producer = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    exist_status = models.CharField(
        max_length=20, choices=[("Available", "Available"), ("Not available", "Not available")]
    )
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.model
