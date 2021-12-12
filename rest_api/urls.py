from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('drivers/driver/', DriverGetData.as_view()),
    path('drivers/driver/<int:pk>/', DriverDetailView.as_view()),
    path('vehicles/vehicle/', VehicleListCreateData.as_view()),
    re_path(r'^vehicles/vehicle/(?P<with_drivers>[yes|no]+)/$', VehicleListCreateData.as_view()),
    path('vehicles/vehicle/<int:pk>/', VehicleDetailView.as_view()),
    path('vehicles/set_driver/<int:pk>/', SetDriverToVehicle.as_view()),
]