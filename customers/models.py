from django.db import models

from datetime import date, timedelta

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    business_category= models.CharField(max_length=100)
    registration_date = models.DateField(default=date.today)
    # age_of_business_in_days = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.name

