from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    timeStamp = models.DateTimeField(verbose_name="Time when added") # add auto_now_add=True for auto set in database
    name= models.CharField(max_length=200)
    price=models.IntegerField(verbose_name="Current base MRP")
    visibleToCostumer= models.BooleanField(verbose_name="should costumer see or not")
    profitPercentage=models.FloatField("Profit ratio")
    item_image=models.ImageField(upload_to="images/", null=True, blank=True) #for only becoz its saying field is required after form submit

    def __str__(self):
        return self.name 
    
    '''
    random permission here,
    it will show in admin user page,
    add to allowed user section to allow this permission for that perticular user
    if view setting will match then it will open the link or forbidden will display
    '''
    class Meta:
        permissions = (('can_read_on_sunday', 'Can read only on sunday of the month'), ("can_manage_privilege", "Can manage privileges"), ('can_read_privilege_detail', 'Can read privilege detail'), )
    

