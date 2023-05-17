from django.contrib import admin
from .models import CarMake, CarModel, CarDealer, DealerReview


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name')

# Register models
admin.site.register(CarMake) 
admin.site.register(CarModel)
admin.site.register(CarDealer)
admin.site.register(DealerReview)
