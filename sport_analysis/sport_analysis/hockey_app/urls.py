from django.urls import path
from .views import PlayerStatusView

app_name = "hockey_app"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('hockey_app/player_status/', PlayerStatusView.as_view()),
    path('hockey_app/player_status/<int:pk>', PlayerStatusView.as_view())
]
