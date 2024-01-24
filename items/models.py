from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=50)

    # it is for displaying name in side bar of admin panal
    class Meta:
        ordering=('name',) # it orders depends on alphabetic names
        verbose_name_plural='Categories'

    # it is for diplay the category name in admin panal
    def __str__(self):
        return self.name

class Item(models.Model):
     category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='items')
     name=models.CharField(max_length=50)
     description=models.TextField(blank=True,null=True)
     price=models.IntegerField()
     image=models.ImageField(upload_to='item_images', height_field=None, width_field=None, max_length=None,blank=True,null=True)
     is_sold=models.BooleanField(default=False)
     created_by=models.ForeignKey(User,on_delete=models.CASCADE,related_name='items')
     created_at=models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.name
