from django.db import models

class MainCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 250,unique=True, null = True, blank = True)
    category_icon = models.ImageField(upload_to ='uploads/', height_field=None, width_field=None, null = True,blank = True)
    def __str__(self):
        return self.name  
  

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length = 250, null = True, blank = True, unique=True)
    ccategory_icon = models.ImageField(upload_to=None, height_field=None, width_field=None, null = True,blank = True)
    subcategories = models.ForeignKey(MainCategory, related_name='category', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
