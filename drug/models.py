from statistics import mode
from django.db import models

# Create your models here.
class Drug(models.Model):
    location = models.CharField(max_length=220)
    time = models.IntegerField()
    PC_healthxp = models.FloatField()
    PC_GDP = models.FloatField()   
    USD_CAP = models.FloatField(null=True)
    Flag_codes = models.CharField(max_length=220, null=True, blank=True)
    Total_spend = models.FloatField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.location)

class Csv(models.Model):
    file_name = models.FileField(upload_to='drug', max_length=100)
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return "File id: {}".format(self.id)

