from django.db import models
from .validators import validate_image


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=10)
    company_name = models.CharField(max_length=200)
    company_description = models.CharField(max_length=100)
    company_image = models.ImageField(upload_to='myimage', validators=[validate_image])
