from django.conf.urls import url

from main import views

app_name = 'main'

urlpatterns = [

    # /modelforms/list

    url(r'^dustbin-list.html$', views.IndexView.as_view(), name='index'),
    url(r'^service-man-list.html$',views.SIndexView.as_view(), name = 'Sindex'),
    url(r'^driver-list.html$', views.DIndexView.as_view(), name = 'Dindex'),
    url(r'^device-list.html$',views.DEIndexView.as_view(), name =' DEindex'),
    url(r'^vehicle-list.html$',views.VIndexView.as_view(), name = 'Vindex'),


    # modelforms/entry
    url(r'^new-dustbin-add-with-location.html$', views.DustbinEntry.as_view(), name='Dustbin-entry'),

    url(r'^add-service-man.html$', views.ServiceEntry.as_view(), name='service-entry'),

    url(r'^add-driver.html$' , views.DriverEntry.as_view(),name='driver-entry'),

    url(r'^add-new-vehicle.html$', views.VehicleEntry.as_view(), name='vehicle-entry'),

    url(r'^add-device.html$',views.DeviceEntry.as_view(),name='device-entry'),





]