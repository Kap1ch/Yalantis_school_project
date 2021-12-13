
# Yalantis_school_project

### Description of the project:

REST API for a fleet of vehicles with drivers.
Created with the django framework, django_rest_framework.

**The project has two models**

+ Driver:
	+ id: int
	+ first_name: str
	+ last_name: str
	+ created_at
	+ updated_at
 
+ Vehicle
	+ id: int
	+ driver_id: FK to Driver
	+ make: str
	+ model: str
	+ plate_number: str  - format example "AA 1234 OO"  
	+ created_at
	+ updated_at 
 
#### List of requests
>**the request body must be passed in json format**


**Driver:**
+ GET /drivers/driver/ - output of the list of drivers
+ GET /drivers/driver/?created_at__gte=10-11-2021 - output of the list of drivers created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - output of the list of drivers created before 16-11-2021
+ GET /drivers/driver/{driver_id}/ - obtaining information on a particular driver
+ POST /drivers/driver/ - creating a new driver
+ UPDATE /drivers/driver/{driver_id}/ - edit driver
+ DELETE /drivers/driver/{driver_id}/ -  delete driver

**Vehicle**
+ GET /vehicles/vehicle/ - output of the list of vehicle
+ GET /vehicles/vehicle/?with_drivers=yes - output of the list of cars with drivers
+ GET /vehicles/vehicle/?with_drivers=no - output of the list of cars without drivers
+ GET /vehicles/vehicle/{vehicle_id} - obtaining information about a specific vehicle 
+ POST /vehicles/vehicle/ - creating a new vehicle 
+ UPDATE /vehicles/vehicle/{vehicle_id}/ - edit vehicle 
+ POST /vehicles/set_driver/{vehicle_id}/ - set the driver in the vehicle / unset the driver from the vehicle  
+ DELETE /vehicles/vehicle/{vehicle_id}/ - delete vehicle




