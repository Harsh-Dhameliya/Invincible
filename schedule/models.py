from django.db import models

class Schedule(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.ForeignKey(
        'package.Package',  # Correct reference to the Customer model
        on_delete=models.CASCADE,
        related_name='Schedule',
        default=None
    ) 
    class meta:
       db_table ="schedule"




   