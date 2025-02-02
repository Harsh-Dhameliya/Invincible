from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class Package(models.Model):
    Package_name = models.CharField(default=None,max_length=30)
    Package_price = models.IntegerField(default=None)
    Total_days = models.IntegerField(default=None)
    Total_nights = models.IntegerField(default=None)
    Package_description =models.TextField(default=None)
    Package_image1 = models.FileField(upload_to='package/',max_length=250,null=True ,default=None)
    Package_image2 = models.FileField(upload_to='package/',max_length=250,null=True ,default=None)
    Package_image3 = models.FileField(upload_to='package/',max_length=250,null=True ,default=None)
    
    category = models.ForeignKey(
        'category.Category',  # Correct reference to the Customer model
        on_delete=models.CASCADE,
        related_name='Package',
        default=None
    )

    Transportation_type = models.ForeignKey(
        'transportation.Transportation',  # Correct reference to the Customer model
        on_delete=models.CASCADE,
        related_name='Package',
        default=None
    )

    
    Guid_name = models.ForeignKey(
        "guide.Guide",
        on_delete=models.CASCADE,
        related_name='Package',
        default=None
    )

    Hotel_name = models.ForeignKey(
        'hotel.Hotel',  # Correct reference to the Customer model
        on_delete=models.CASCADE,
        related_name='Package',
        default=None
    )
    Slug = AutoSlugField(populate_from='Package_name',default=None)

    def __str__(self):
        return self.Total_days

    class meta:
        db_table ='package'



