import datetime

from django.db import models
from django.utils.timezone import now


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="Brand")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to="images", null=True)

    # M-O: https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Request(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(
        max_length=200, null=True, verbose_name="Description"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, verbose_name="Category"
    )
    image = models.ImageField(
        upload_to="images/request/", null=True, verbose_name="product_image"
    )
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, null=True, verbose_name="Brand"
    )
    date_creation = models.DateField(verbose_name="Fecha de inicio", default=now)
    aggregate = models.BooleanField(verbose_name="aggregate product", default=False)

    def soft_delete(self):
        self.aggregate = True
        super().save()

    # def delete(self, using=None, keep_parents=False):
    #     self.image.storage.delete(self.image.name)
    #     super().delete()
