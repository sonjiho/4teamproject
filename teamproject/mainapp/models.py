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
    addr = models.CharField(max_length=45)
    lon = models.IntegerField()
    lat = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"id={self.id}, name{self.name}, addr{self.addr}, lon{self.lon},lat{self.lat}, city{self.city}, type{self.type}"

class DMap(models.Model):
    major_class = models.CharField(max_length=20)
    sub_class = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    road_name = models.CharField(max_length=50)
    latlng = models.CharField(max_length=50)
    etc = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name + ":" + str(self.city) + " " + str(self.state) + " " + str(self.road_name)