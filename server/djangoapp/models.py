from django.db import models
from django.utils.timezone import now


# Create your models here.

# Create a Car Make model 
class CarMake(models.Model):
    cmname = models.CharField(null=False, max_length=100, default='Enter Make Name...')
    description = models.CharField(max_length=500)

    def __str__(self):
        return "Name: " + self.cmname + "," + \
            "Description: " + self.description



# Create a Car Model model 
class CarModel(models.Model):
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "WAGON"
    MAKE_TYPE = [
        (SEDAN, "Sedan"),
        (SUV, "SUV"),
        (WAGON, "WAGON"),
    ]
    cname = models.CharField(null=False, max_length=100, default='Enter Model Name...')
    dealerid = models.IntegerField()
    cartype = models.CharField(
        max_length=200,
        choices=MAKE_TYPE,
        default=SEDAN,
    )
    year = models.DateField(null=True)
    carmakes = models.ManyToManyField(CarMake)

    def __str__(self):
        return self.cname


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer(models.Model):
    cardealer_name = models.CharField(max_length=200, default="Enter Name...")
    description = models.CharField(max_length=500)


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    dealerreview_name = models.CharField(max_length=200, default="Enter Name...")
    description = models.CharField(max_length=500)