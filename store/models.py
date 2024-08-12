from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    def __str__(self):
        return self.name
    
    
class gold(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    texts = models.TextField(blank=True)

    def __str__(self):
        return self.name
class gold1(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    texts = models.TextField(blank=True)

    def __str__(self):
        return self.name


    
class product(models.Model):
    game = models.ForeignKey(Game, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE )
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    in_stock = models.BooleanField(default=True)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ('-created')

    def __str__(self):
        return self.title


    


