from django.contrib import admin

# Register your models here.
from .models import Dustbin,service,driver,device,vehicle
admin.site.register(Dustbin)
admin.site.register(service)
admin.site.register(device)
admin.site.register(driver)
admin.site.register(vehicle)
