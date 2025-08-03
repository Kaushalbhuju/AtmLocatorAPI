from django.db import models

class ATM(models.Model):
    bank_name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_functional = models.BooleanField(default=True)
    has_cash = models.BooleanField(default=True)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bank_name} ATM at {self.location}"
