from django.db import models

# Create your models here.

class Bizning_taklif(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Biz_kimmiz(models.Model):
    photo = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=100)
    jobs = models.CharField(max_length=100)
    informations = models.TextField()

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class Slaidshow(models.Model):
    photo = models.ImageField(upload_to='images/',blank=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description
