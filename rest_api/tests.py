from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Driver, Vehicle
from .serializers import DriverSerializer, VehicleSerializer
# Create your tests here.


class DriverApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.first_driver = Driver.objects.create(
            first_name='name_one',
            last_name='last_name_one',
        )
        self.second_driver = Driver.objects.create(
            first_name='name_two',
            last_name='last_name_two',
        )
        self.third_driver = Driver.objects.create(
            first_name='name_three',
            last_name='last_name_three',
        )

    def test_driver_list_get(self):
        url = '/drivers/driver/'
        response = self.client.get(url, format='json')
        serializer_data = DriverSerializer([self.first_driver, self.second_driver, self.third_driver], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_driver_get(self):
        url = '/drivers/driver/{}/'.format(self.first_driver.id)
        response = self.client.get(url, format='json')
        serializer_data = DriverSerializer(self.first_driver).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_driver_get_list_gte(self):
        url = '/drivers/driver/?created_at__gte=10-11-2021'
        response = self.client.get(url, format='json')
        serializer_data = DriverSerializer([self.first_driver, self.second_driver, self.third_driver], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_driver_get_list_lte(self):
        url = '/drivers/driver/?created_at__lte=16-11-2021'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_driver_post(self):
        url = '/drivers/driver/'
        data = {
            'first_name': 'test_first_name',
            'last_name': 'test_last_name'
        }
        response = self.client.post(url, data, format='json')
        date = datetime.now().date().strftime('%d-%m-%Y')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 4,
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'created_at': date,
            'update_at': date
        })

    def test_driver_put(self):
        url = '/drivers/driver/{}/'.format(self.first_driver.id)
        data = {
            'first_name': 'test_first_name_put',
            'last_name': 'test_last_name_put'
        }
        response = self.client.put(url, data, format='json')
        date = datetime.now().date().strftime('%d-%m-%Y')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'first_name': 'test_first_name_put',
            'last_name': 'test_last_name_put',
            'created_at': date,
            'update_at': date
        })

    def test_driver_delete(self):
        url = '/drivers/driver/{}/'.format(self.first_driver.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.first_driver, Driver.objects.all())


class DriverApiFailedTestCase(APITestCase):
    def setUp(self) -> None:
        self.first_driver = Driver.objects.create(
            first_name='first_name',
            last_name='last_name',
        )

    def test_driver_get_failed(self):
        url = '/drivers/driver/1000/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_driver_get_gte_failed(self):
        url = '/drivers/driver/?created_at__gte=2021.11/10'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_driver_get_lte_failed(self):
        url = '/drivers/driver/?created_at__gte=2021.11/16'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_driver_delete_failed(self):
        url = '/drivers/driver/1000/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(self.first_driver, Driver.objects.all())


class VehicleApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.driver = Driver.objects.create(
            first_name='first_name',
            last_name='last_name',
        )
        self.first_vehicle = Vehicle.objects.create(
            driver_id=self.driver,
            make='make_one',
            model='model_one',
            plate_number='AA 1234 AA'
        )
        self.second_vehicle = Vehicle.objects.create(
            driver_id=None,
            make='make_two',
            model='model_two',
            plate_number='BB 1234 BB'
        )
        self.third_vehicle = Vehicle.objects.create(
            driver_id=self.driver,
            make='make_three',
            model='model_three',
            plate_number='CC 1234 CC'
        )

    def test_vehicle_get_list(self):
        url = '/vehicles/vehicle/'
        response = self.client.get(url, format='json')
        serializer_data = VehicleSerializer([self.first_vehicle,
                                             self.second_vehicle,
                                             self.third_vehicle], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_vehicle_get(self):
        url = '/vehicles/vehicle/{}/'.format(self.first_vehicle.id)
        response = self.client.get(url, format='json')
        serializer_data = VehicleSerializer(self.first_vehicle).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_vehicle_get_list_yes(self):
        url = '/vehicles/vehicle/?with_drivers=yes'
        response = self.client.get(url, format='json')
        serializer_data = VehicleSerializer([self.first_vehicle, self.third_vehicle], many=True).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_vehicle_get_list_no(self):
        url = '/vehicles/vehicle/?with_drivers=no'
        response = self.client.get(url, format='json')
        serializer_data = VehicleSerializer(self.second_vehicle).data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [serializer_data])

    def test_vehicle_post(self):
        url = '/vehicles/vehicle/'
        data = {
            'driver_id': self.driver.id,
            'make': 'new_make',
            'model': 'new_model',
            'plate_number': 'DD 1234 DD'
        }
        response = self.client.post(url, data, format='json')
        date = datetime.now().date().strftime('%d-%m-%Y')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 4,
            'driver_id': self.driver.id,
            'make': 'new_make',
            'model': 'new_model',
            'plate_number': 'DD 1234 DD',
            'created_at': date,
            'update_at': date
        })

    def test_vehicle_post_update_one(self):
        url = '/vehicles/set_driver/{}/'.format(self.first_vehicle.id)
        data = {
            'id': self.driver.id
        }
        response = self.client.post(url, data, format='json')
        date = datetime.now().date().strftime('%d-%m-%Y')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 1,
            'driver_id': None,
            'make': 'make_one',
            'model': 'model_one',
            'plate_number': 'AA 1234 AA',
            'created_at': date,
            'update_at': date
        })

    def test_vehicle_post_update_two(self):
        url = '/vehicles/set_driver/{}/'.format(self.second_vehicle.id)
        data = {
            'id': self.driver.id
        }
        response = self.client.post(url, data, format='json')
        date = datetime.now().date().strftime('%d-%m-%Y')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 2,
            'driver_id': self.driver.id,
            'make': 'make_two',
            'model': 'model_two',
            'plate_number': 'BB 1234 BB',
            'created_at': date,
            'update_at': date
        })

    def test_vehicle_put(self):
        url = '/vehicles/vehicle/{}/'.format(self.first_vehicle.id)
        data = {
            'driver_id': None,
            'make': 'make_one_update',
            'model': 'model_one_update',
            'plate_number': 'AD 4321 AD'
        }
        response = self.client.put(url, data, format='json')
        date = datetime.now().date().strftime('%d-%m-%Y')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': 1,
            'driver_id': None,
            'make': 'make_one_update',
            'model': 'model_one_update',
            'plate_number': 'AD 4321 AD',
            'created_at': date,
            'update_at': date
        })

    def test_vehicle_delete(self):
        url = '/vehicles/vehicle/{}/'.format(self.first_vehicle.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.first_vehicle, Vehicle.objects.all())


class VehicleApiFailedTestCase(APITestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle.objects.create(
            make='make_one',
            model='model_one',
            plate_number='AA 1234 AA'
        )

    def test_vehicle_get(self):
        url = '/vehicles/vehicle/1000/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vehicle_get_with_driver(self):
        url = '/vehicles/vehicle/?with_drivers=jhfjfhd'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vehicle_post_create_number_repeat(self):
        url = '/vehicles/vehicle/'
        data = {
            'make': 'make_failed',
            'model': 'model_failed',
            'plate_number': 'AA 1234 AA'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vehicle_post_create_number(self):
        url = '/vehicles/vehicle/'
        data = {
            'make': 'make_failed',
            'model': 'model_failed',
            'plate_number': 'ds 2345 gr'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vehicle_post_update_id(self):
        url = '/vehicles/set_driver/1000/'
        data = {
            'id': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vehicle_post_update_driver_id(self):
        url = '/vehicles/set_driver/{}/'.format(self.vehicle.id)
        data = {
            'id': 1000
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_vehicle_put_id(self):
        url = '/vehicles/vehicle/1000/'.format(self.vehicle.id)
        data = {
            'plate_number': 'AA 1234 AA'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_vehicle_put_failed_number_repeat(self):
        url = '/vehicles/vehicle/{}/'.format(self.vehicle.id)
        data = {
            'plate_number': 'AA 1234 AA'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_id(self):
        url = '/vehicles/vehicle/1000/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn(self.vehicle, Vehicle.objects.all())







