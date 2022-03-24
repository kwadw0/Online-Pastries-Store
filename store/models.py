from audioop import reverse
from distutils.command.upload import upload
from django.db import models
import uuid

class Product(models.Model):
    name = models.CharField(max_length=200,)
    price = models.DecimalField(max_digits=4,  decimal_places=2)
    images = models.ImageField(upload_to='covers/', blank=True)
    id = models.URLField(primary_key=True, default=uuid.uuid4,  editable=False,)
    description = models.TextField(max_length=100,)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs = {'pk': str(self.pk)})

# Create your models here.
