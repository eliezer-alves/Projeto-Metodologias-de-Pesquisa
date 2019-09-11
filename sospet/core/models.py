from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    city = models.CharField(max_length=100, null=True)
    bedrooms = models.IntegerField(default=0)
    toilets = models.IntegerField(default=0)
    peoples = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    description = models.TextField(null=True)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(null=True)
    begin_date = models.DateField(auto_now_add=True,blank=True, null=True)
    photo = models.ImageField(upload_to='pet', null=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Pets'
        db_table = 'pet'


