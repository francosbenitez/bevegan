from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images")

    # M-O: https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
