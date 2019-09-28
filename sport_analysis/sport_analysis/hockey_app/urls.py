from rest_framework.routers import DefaultRouter

from .views import PlayerStatusViewSet

router = DefaultRouter()
router.register(r'hockey_app/player_status', PlayerStatusViewSet)

urlpatterns = router.urls
