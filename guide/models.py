from django.db import models

class Guide(models.Model):
    g_name = models.CharField(max_length=20)
    g_lang = models.CharField(max_length=20)
    g_experience = models.CharField(max_length=20)

    def __str__(self):
        return self.g_name
    
    class meta:
        db_table ='guide'



