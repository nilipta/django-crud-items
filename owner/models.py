from django.db import models

# Create your models here.
class Item(models.Model):
    timeStamp = models.DateTimeField(verbose_name="Time when added") # add auto_now_add=True for auto set in database
    name= models.CharField(max_length=200)
    price=models.IntegerField(verbose_name="Current base MRP")
    visibleToCostumer= models.BooleanField(verbose_name="should costumer see or not")
    profitPercentage=models.FloatField("Profit ratio")
    item_image=models.ImageField(upload_to="images/", null=True, blank=True) #for only becoz its saying field is required after form submit


    def __str__(self):
        return self.name 

