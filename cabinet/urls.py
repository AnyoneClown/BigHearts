from rest_framework import routers

from cabinet.views import PostViewSet

router = routers.DefaultRouter()
router.register("posts", PostViewSet)

urlpatterns = router.urls

app_name = "cabinet"
