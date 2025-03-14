from django.db import models

class Bookings(models.Model):
    
    customer_id = models.IntegerField(default=None)
    name = models.CharField(default=None, max_length=30)
    mobile_no = models.CharField(default=None,max_length=10)
    birth_date = models.DateField(default=None)
    gender = models.CharField(default=None, max_length=10)

    class meta:
        db_table = "booking"



    
