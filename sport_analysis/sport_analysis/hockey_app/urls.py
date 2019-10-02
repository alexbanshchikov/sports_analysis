from rest_framework.routers import DefaultRouter

from .views import PlayerStatusViewSet, AmpluaViewSet, ConferenceViewSet, DivisionViewSet, TimePeriodViewSet, \
    TeamViewSet, GameStatsViewSet, GameViewSet, GameGoalsViewSet, GamePenaltiesViewSet, MannerOfPlayViewSet, \
    AfterGameBullitsViewSet, CoachViewSet, CoachInTeamViewSet, DerbiViewSet, GoalShootsViewSet, GoalkeeperStatsViewSet, \
    OffenceStatsViewSet, PersonalEnemyViewSet, PlayerViewSet, PlayerInTeamViewSet, RefereeViewSet, RefereeInGameViewSet, \
    TeamInConferenceViewSet, TeamInDivisionViewSet, TeamPenaltiesViewSet, TeamStatsByPeriodViewSet, TeamStatsByStrengthViewSet, \
    MannerOfPlayInTeamViewSet

router = DefaultRouter()
router.register(r'hockey_app/player_status', PlayerStatusViewSet)
router.register(r'hockey_app/amplua', AmpluaViewSet)
router.register(r'hockey_app/conference', ConferenceViewSet)
router.register(r'hockey_app/division', DivisionViewSet)
router.register(r'hockey_app/time_period', TimePeriodViewSet)
router.register(r'hockey_app/team', TeamViewSet)
router.register(r'hockey_app/game_stats', GameStatsViewSet)
router.register(r'hockey_app/game', GameViewSet)
router.register(r'hockey_app/game_goals', GameGoalsViewSet)
router.register(r'hockey_app/game_penalties', GamePenaltiesViewSet)
router.register(r'hockey_app/manner_of_play', MannerOfPlayViewSet)
router.register(r'hockey_app/after_game_bullits', AfterGameBullitsViewSet)
router.register(r'hockey_app/coach', CoachViewSet)
router.register(r'hockey_app/coach_in_team', CoachInTeamViewSet)
router.register(r'hockey_app/derbi', DerbiViewSet)
router.register(r'hockey_app/goal_shoot', GoalShootsViewSet)
router.register(r'hockey_app/goalkeeper_stats', GoalkeeperStatsViewSet)
router.register(r'hockey_app/offence_stats', OffenceStatsViewSet)
router.register(r'hockey_app/personal_enemy', PersonalEnemyViewSet)
router.register(r'hockey_app/player', PlayerViewSet)
router.register(r'hockey_app/player_in_team', PlayerInTeamViewSet)
router.register(r'hockey_app/referee', RefereeViewSet)
router.register(r'hockey_app/referee_in_game', RefereeInGameViewSet)
router.register(r'hockey_app/team_in_conference', TeamInConferenceViewSet)
router.register(r'hockey_app/team_in_division', TeamInDivisionViewSet)
router.register(r'hockey_app/team_penalties', TeamPenaltiesViewSet)
router.register(r'hockey_app/team_stats_by_period', TeamStatsByPeriodViewSet)
router.register(r'hockey_app/team_stats_by_strength', TeamStatsByStrengthViewSet)
router.register(r'hockey_app/manner_of_play_in_team', MannerOfPlayInTeamViewSet)

urlpatterns = router.urls
