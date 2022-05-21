from django.db import models


# Create your models here.
class Team(models.Model):
    """ X """

    name = models.CharField(max_length=60)
    description = models.TextField()
    role = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Location(models.Model):
    """ X """
    address = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.address


class Contact(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    email = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name
