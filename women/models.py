from django.db import models

# Create your models here.


class Women(models.Model):
    title = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    is_published = models.BooleanField(default=False)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    car = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.title},{self.second_name}'


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
