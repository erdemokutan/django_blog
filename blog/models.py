from django.db import models
from django.utils.text import slugify

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    image=models.CharField(max_length=50)
    description=models.TextField()
    is_active=models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True, unique=True ,db_index=True, editable=False)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


