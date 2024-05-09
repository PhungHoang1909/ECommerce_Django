from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Product (models.Model):
    primary_key = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

    name = models.CharField(max_length=50)
    slug = models.SlugField()

    description = models.TextField(blank = True, null = True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
