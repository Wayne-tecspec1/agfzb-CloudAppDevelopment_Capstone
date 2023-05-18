from django.db import models
from django.utils.timezone import now



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
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip
    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview(models.Model):
    dealerreview_name = models.CharField(max_length=200, default="Enter Name...")
    description = models.CharField(max_length=500)