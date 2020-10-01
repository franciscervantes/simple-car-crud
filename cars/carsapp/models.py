from django.db import models

# Create your models here.

class Cars(models.Model):
    car_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    class Meta:
        db_table = 'cars'