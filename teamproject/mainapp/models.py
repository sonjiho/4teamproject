from django.db import models


class State(models.Model):
    statename = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, statename={self.statename}"


class City(models.Model):
    cityname = models.CharField(max_length=200)
    state = models.OneToOneField(State, on_delete=models.CASCADE)

    def __str__(self):
        return F"id={self.id}, cityname={self.cityname}, state={self.state}"


class Category(models.Model):
    categoryname = models.CharField(max_length=200)

    def __str__(self):
        return f"id={self.id}, categoryname={self.categoryname}"


class Type(models.Model):
    typename = models.CharField(max_length=200)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"id={self.id}, typename={self.typename}"


class Dogplace(models.Model):
    name = models.CharField(max_length=200)
    addr = models.CharField(max_length=200)
    lon = models.IntegerField()
    lat = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"id={self.id}, name{self.name}, addr{self.addr}, lon{self.lon},lat{self.lat}, city{self.city}, type{self.type}"
