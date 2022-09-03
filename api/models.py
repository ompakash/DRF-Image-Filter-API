from django.db import models

# Create your models here.
class ImageFilter(models.Model):
    name = models.CharField(max_length=200)
    before_img = models.ImageField(upload_to='before_images',blank=False)

    def __str__(self):
        return self.name
