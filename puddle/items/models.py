from django.contrib.auth.models import User
from django.db import models

class category(models.Model):
    name = models.CharField(max_length=255) 

    class Meta:
        ordering = ("name", )
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class item(models.Model):
    category = models.ForeignKey(category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255) 
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item-image',blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name