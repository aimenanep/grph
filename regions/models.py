from django.db import models


class Country(models.Model):
    name=models.CharField(max_length=255)
    arabic_name=models.CharField(max_length=255)
    code=models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Region(models.Model):
    name=models.CharField(max_length=255)
    arabic_name=models.CharField(max_length=255)
    code=models.CharField(max_length=3)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name=models.CharField(max_length=255)
    arabic_name=models.CharField(max_length=255)
    postal_code=models.CharField(max_length=255,blank=True,null=True)
    region=models.ForeignKey(Region,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
