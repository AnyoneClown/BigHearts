from rest_framework import routers

from cabinet.views import PostViewSet, DeliveryViewSet, ServiceViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)
router.register("deliveries", DeliveryViewSet)
router.register("services", ServiceViewSet)

urlpatterns = router.urls

app_name = "cabinet"
