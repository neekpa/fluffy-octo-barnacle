from django.shortcuts import render

# Create your views here.
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
from main.models import Dustbin, service ,driver ,device , vehicle
'''''''''
from django.shortcuts import render
from django.http import HttpResponse
from .models import service
from .forms import serviceForm
from django.shortcuts import redirect


def index(request):
    services = service.objects.all()
    return render(request, 'main/service-man-list.html', {'services': services})


def add_new_service(request):
    form = serviceForm()
    if request.method == 'POST':
        form = serviceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            contact_no = form.cleaned_data['contact_no']
            p = service.objects.create(name=name, contact_no=contact_no)

            if p.pk > 0:
                return redirect('index')
    return render(request, 'main/add-service-man.html', {'form': form})


'''''''''

# view for the index page
class IndexView(generic.ListView):
    # name of the object to be used in the index.html
    context_object_name = 'Dustbin_list'
    template_name = 'main/dustbin-list.html'

    def get_queryset(self):
        return Dustbin.objects.all()

# view for the product entry page
class   DustbinEntry(CreateView):
    model = Dustbin
    # the fields mentioned below become the entry rows in the generated form
    fields = ['dustbin_no', 'weight', 'expiry', 'comment','location','RFID_TAG']

class SIndexView(generic.ListView):
    # name of the object to be used in the service_man_list.html
    context_object_name = 'service_list'
    template_name = 'main/service-man-list.html'
    def get_queryset(self):
        return service.objects.all()

# view for the service entry page
class ServiceEntry(CreateView):
    model = service
    # the fields mentioned below become the entry rows in the generated form
    fields = ['name', 'email_id', 'adhar_card_no','service_type','contact_no']


class DIndexView(generic.ListView):
    # name of the object to be used in the service_man_list.html
    context_object_name = 'driver_list'
    template_name = 'main/driver-list.html'
    def get_queryset(self):
        return driver.objects.all()

#view for the driver entry page
class DriverEntry(CreateView):
    model = driver
    # the fields mentioned below become the entry rows in the generated form   'Front_A','Back_A  'Front_L','Back_L'
    fields = ['driver_name', 'Email_id', 'adhar_card_no','Driving_lisence_no',
              'Date_of_expiry','contact_no']

class DEIndexView(generic.ListView):
    # name of the object to be used in the service_man_list.html
    context_object_name = 'device_list'
    template_name = 'main/device-list.html'
    def get_queryset(self):
        return device.objects.all()


#view for the device entry page
class DeviceEntry(CreateView):
    model = device
    # the fields mentioned below become the entry rows in the generated form
    fields = ['device_name', 'Type', 'Device_use','Quantity']

class VIndexView(generic.ListView):
    # name of the object to be used in the service_man_list.html
    context_object_name = 'vehicle_list'
    template_name = 'main/vehicle-list.html'
    def get_queryset(self):
        return vehicle.objects.all()

class VehicleEntry(CreateView):
    model = vehicle
    # the fields mentioned below become the entry rows in the generated form
    fields = ['vehicle_type', 'capacity', 'area','vehicle_no','rfid_kit_no']






'''''''''

# view for the product update page
class ProductUpdate(UpdateView):
    model = Product
    # the fields mentioned below become the entry rows in the update form
    fields = ['dustbin_no', 'weight', 'expiry','comment','location','RFID_TAG']


# view for deleting a product entry
class ProductDelete(DeleteView):
    model = Product
    # the delete button forwards to the url mentioned below.
    success_url = reverse_lazy('modelforms:index')'''''

