# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


#@api_view(['GET', 'POST'])
# def smart_home(request):
#     if request.method == 'GET':
#         sensors = Sensor.objects.all()
#         res = SensorSerializer(sensors, many=True)
#         return Response(res.data)
#     if request.method == 'POST':
#         return Response({'status': 'ok'})


# class Smart_home_View(ModelViewSet):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         res = SensorSerializer(sensors, many=True)
#         return Response(res.data)
#
#     def post(self, request):
#         Sensors = SensorSerializer(data=request.data)
#         name = request.data.get('name')
#         description = request.data.get('description')
#         Sensors = Sensor.objects.update(
#              name, description
#         )
#         return Response(Sensors)

# class SensorsView(ModelViewSet):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorSerializer

class Smart_home_View(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasurementView(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer