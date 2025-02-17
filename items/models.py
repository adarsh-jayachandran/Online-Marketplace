from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#user: root pass:root
class Category(models.Model):
    name = models.CharField(max_length=255)


    def __str__(self): # for our items name to be appeared on the database
        return self.name

    class Meta: #this step is to correctly spell the name of the table in the database
        verbose_name_plural = 'Categories' 
        ordering = ('name',) # for ordering by name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image= models.ImageField(upload_to='item_images', blank=True  ,null= True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField()






