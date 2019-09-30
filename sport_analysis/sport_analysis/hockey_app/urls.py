from rest_framework.routers import DefaultRouter

from .views import PlayerStatusViewSet, AmpluaViewSet, ConferenceViewSet, DivisionViewSet, TimePeriodViewSet

router = DefaultRouter()
router.register(r'hockey_app/player_status', PlayerStatusViewSet)
router.register(r'hockey_app/amplua', AmpluaViewSet)
router.register(r'hockey_app/conference', ConferenceViewSet)
router.register(r'hockey_app/division', DivisionViewSet)
router.register(r'hockey_app/time_period', TimePeriodViewSet)

urlpatterns = router.urls
