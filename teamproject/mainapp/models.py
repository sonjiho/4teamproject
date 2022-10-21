from django.db import models

class State(models.Model):
    statename = models.CharField(max_length=45)
    def __str__(self):
        return f"id={self.id}, statename={self.statename}"

class City(models.Model):
    cityname = models.CharField(max_length=45)
    state = models.OneToOneField(State, on_delete=models.CASCADE)
    def __str__(self):
        return F"id={self.id}, cityname={self.cityname}, state={self.state}"

class Category(models.Model):
    categoryname = models.CharField(max_length=45)
    def __str__(self):
        return f"id={self.id}, categoryname={self.categoryname}"


class Type(models.Model):
    typename = models.CharField(max_length=45)
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"id={self.id}, typename={self.typename}"

class Dogplace(models.Model):
    name = models.CharField(max_length=45)
    addrone = models.CharField(max_length=45)
    addrtwo = models.CharField(max_length=45)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"id={self.id}, name{self.name}, addrone{self.addrone}, addrtwo{self.addrtwo}, city{self.city}, type{self.type}"