from django.db import models

class Hotel(models.Model):
    h_name = models.CharField(max_length=50)

    def __str__(self):
        return self.h_name
    
    class meta:
        db_table = 'hotel'
