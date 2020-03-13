from django.contrib import admin
from .models import (
    OrderSpecification,
    car_size,
    DriverInformation,
    Support_Spec,
    Shipment_orderModel,
    LocationModel,
)

# Register your models here.

admin.site.register(LocationModel)
admin.site.register(OrderSpecification)
admin.site.register(car_size)
admin.site.register(DriverInformation)
admin.site.register(Support_Spec)
admin.site.register(Shipment_orderModel)