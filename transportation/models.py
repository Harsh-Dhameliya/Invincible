from django.db import models

class Transportation(models.Model):
    t_name = models.CharField(max_length=50)

    def __str__(self):
        return self.t_name
    
    class meta:
        db_table = 'transportation'

    
    
