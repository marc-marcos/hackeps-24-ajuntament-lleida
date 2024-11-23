from rest_framework import routers
from .views import (
    ParkingViewSet,
    PlantaViewSet,
    PlazaViewSet,
    PlazaLogViewSet,
)


router = routers.DefaultRouter()

router.register(r"parking", ParkingViewSet)
router.register(r"planta", PlantaViewSet)
router.register(r"plaza", PlazaViewSet)
router.register(r"plazalog", PlazaLogViewSet)

urlpatterns = router.urls
