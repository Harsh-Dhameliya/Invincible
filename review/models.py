from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=15)
    review = models.TextField(max_length=400)


    
    class meta:
        db_table = "review"