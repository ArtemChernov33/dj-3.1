from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import Smart_home_View, MeasurementView


router = DefaultRouter()
router.register('measurements', MeasurementView)
# router.register('sensors/<pk>', SensorsView)
router.register('sensors', Smart_home_View)


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('smart_home/', Smart_home_View),
    # path('sensors/<pk>/', SensorsView),
    path('smart_home/', include(router.urls)),
]

# urlpatterns = router.urls