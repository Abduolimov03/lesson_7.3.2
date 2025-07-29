from django.db import models

class Macbook(models.Model):
    model = models.CharField(max_length=20)
    size = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.model
