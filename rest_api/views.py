from rest_framework.views import Response
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from .serializers import DriverSerializer, VehicleSerializer
from .models import Driver, Vehicle
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from .service import DriverFilter


class DriverGetData(generics.ListCreateAPIView):
    serializer_class = DriverSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DriverFilter

    queryset = Driver.objects.all()


class DriverDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()


class VehicleListCreateData(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        with_drivers = self.request.query_params.get('with_drivers')
        if with_drivers is None:
            return queryset
        if with_drivers.lower() == 'yes':
            queryset = Vehicle.objects.filter(driver_id__isnull=False)
            return queryset
        elif with_drivers.lower() == 'no':
            queryset = Vehicle.objects.filter(driver_id=None)
            return queryset
        raise ValidationError


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class SetDriverToVehicle(generics.CreateAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()

    def post(self, request, *args, **kwargs):
        return self.update_car_driver(request, **kwargs)

    def update_car_driver(self, request, **kwargs):
        kwargs['partial'] = True

        instance = self.get_object()
        if instance.driver_id:
            instance.driver_id = None
            serializer = self.get_serializer(instance, data=request.data, partial=kwargs['partial'])
            serializer.is_valid(raise_exception=True)
            serializer.save()
        else:
            try:
                instance.driver_id = Driver.objects.get(id=int(request.data['id']))
                serializer = self.get_serializer(instance, data=request.data, partial=kwargs['partial'])
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Driver.DoesNotExist:
                 return Response({'error': 'a driver with this id does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
