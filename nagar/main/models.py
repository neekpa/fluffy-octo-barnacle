
# Create your models here.
from django.db import models

# Create your models here.
from django.urls import reverse

TYPE = (
    ('VEHICLE', 'veh'),
    ('DUSTBIN', 'dust'),

)

VEHICLE_TYPE = (
    ('Mini', 'mini'),
    ('MICRO','micro'),
    ('SEDAN','sedan'),
    ('SUV','suv'),

)

class Dustbin(models.Model):
    dustbin_no = models.IntegerField()
    weight = models.IntegerField()
    expiry = models.IntegerField()
    comment = models.TextField(max_length=500)
    location = models.CharField(max_length=40)
    RFID_TAG = models.IntegerField()


    # on submit click on the product entry page, it redirects to the url below.
    #return a URL string that would point to this model's view
    def get_absolute_url(self):
        return reverse('main:index')


    class Meta:
        db_table = "Dustbin"



class service(models.Model):
    name = models.CharField(max_length=20)
    email_id = models.EmailField()
    adhar_card_no = models.CharField(max_length=12)
    service_type = models.CharField(max_length=3)
    contact_no = models.IntegerField()

    def get_absolute_url(self):
        return reverse('main:Sindex')


    class Meta:
        db_table = "service"


class driver(models.Model):
    driver_name = models.CharField(max_length=20)
    Email_id = models.CharField(max_length=20)
    adhar_card_no = models.IntegerField()
    Front_A = models.ImageField(upload_to='front/')
    Back_A = models . ImageField(upload_to='back/')
    Driving_lisence_no = models . IntegerField()
    Front_L = models.ImageField(upload_to='front/')
    Back_L = models.ImageField(upload_to='back/')
    Date_of_expiry = models.IntegerField()
    contact_no = models.IntegerField()

    def get_absolute_url(self):
        return reverse('main:Dindex')


    class Meta:
        db_table = "driver"


class device(models.Model):
    device_name = models.CharField(max_length=20)
    Type = models.CharField(max_length=2 , choices=TYPE)
    Device_use = models.CharField(max_length=1)
    Quantity=models.IntegerField()

    def get_absolute_url(self):
        return reverse('main DEindex')


    class Meta:
        db_table = "device"

class vehicle(models.Model):
    vehicle_type = models.CharField(max_length=20,choices=VEHICLE_TYPE)                               #ForeignKey(vehicle, on_delete=models.SET_NULL, null=True)
    capacity = models.IntegerField()
    area = models.IntegerField()
    vehicle_no = models.IntegerField()
    rfid_kit_no = models.IntegerField()

    def get_absolute_url(self):
        return reverse('main:Vindex')


    class Meta:
        db_table = "vehicle"
