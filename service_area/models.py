from django.db import models
from provider.models import Provider

# Create your models here.


class ServiceArea(models.Model):
    name = models.CharField(max_length=64, unique=True)
    price = models.IntegerField()
    long = models.DecimalField(max_digits=8, decimal_places=5)
    lat = models.DecimalField(max_digits=8, decimal_places=5)
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{0} | Location: ({1},{2})".format(
                                            self.name,
                                            str(self.lat), 
                                            str(self.long))
    
    @property
    def cordinates(self):
        return (self.lat, self.long)
