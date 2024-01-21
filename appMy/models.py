from django.db import models

# Create your models here.

class Category(models.Model):
   title = models.CharField(("Kategori"), max_length=50)
   slug = models.SlugField(("Slug"))

   def __str__(self):
       return self.title
   
class Dizi(models.Model):
   title = models.CharField(("Dizi"), max_length=50)
   slug = models.SlugField(("Slug"))
   category = models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE)
   populer = models.BooleanField(("Yeni Ve Populer Mi"), default=False)
   image = models.ImageField(("Dizi Resmi"), upload_to="dizi", max_length=250)

   def __str__(self):
       return self.title