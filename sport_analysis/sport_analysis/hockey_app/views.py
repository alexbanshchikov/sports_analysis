from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PlayerStatusSerializer, AmpluaSerializer, ConferenceSerializer, DivisionSerializer, TimePeriodSerializer, \
    TeamSerializer, GameStatsSerializer, GameSerializer, GameGoalsSerializer, GamePenaltiesSerializer, \
    MannerOfPlaySerializer, AfterGameBullitsSerializer, CoachSerializer, CoachInTeamSerializer, DerbiSerializer, GoalShootsSerializer, \
    GoalkeeperStatsSerializer, OffenceStatsSerializer, PersonalEnemySerializer, PlayerSerializer, PlayerInTeamSerializer, \
    RefereeSerializer, RefereeInGameSerializer, TeamInConferenceSerializer, TeamInDivisionSerializer, TeamPenaltiesSerializer, \
    TeamStatsByPeriodSerializer, TeamStatsByStrengthSerializer, MannerOfPlayInTeamSerializer
from .models import PlayerStatus, Amplua, Conference, Division, TimePeriod, Team, GameStats, Game, GameGoals, GamePenalties, \
    MannerOfPlay, AfterGameBullits, Coach, CoachInTeam, Derbi, GoalShoots, GoalkeeperStats, OffenceStats, PersonalEnemy, \
    Player, PlayerInTeam, Referee, RefereeInGame, TeamInDivision, TeamInConference, TeamPenalties, TeamStatsByPeriod, \
    TeamStatsByStrength, MannerOfPlayInTeam


class PlayerStatusViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerStatusSerializer
    queryset = PlayerStatus.objects.all()


class AmpluaViewSet(viewsets.ModelViewSet):
    serializer_class = AmpluaSerializer
    queryset = Amplua.objects.all()


class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    queryset = Conference.objects.all()


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()


class TimePeriodViewSet(viewsets.ModelViewSet):
    serializer_class = TimePeriodSerializer
    queryset = TimePeriod.objects.all()


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class GameStatsViewSet(viewsets.ModelViewSet):
    serializer_class = GameStatsSerializer
    queryset = GameStats.objects.all()


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = GameGoalsSerializer
    queryset = GameGoals.objects.all()


class GamePenaltiesViewSet(viewsets.ModelViewSet):
    serializer_class = GamePenaltiesSerializer
    queryset = GamePenalties.objects.all()


class MannerOfPlayViewSet(viewsets.ModelViewSet):
    serializer_class = MannerOfPlaySerializer
    queryset = MannerOfPlay.objects.all()


class AfterGameBullitsViewSet(viewsets.ModelViewSet):
    serializer_class = AfterGameBullitsSerializer
    queryset = AfterGameBullits.objects.all()


class CoachViewSet(viewsets.ModelViewSet):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()


class CoachInTeamViewSet(viewsets.ModelViewSet):
    serializer_class = CoachInTeamSerializer
    queryset = CoachInTeam.objects.all()


class DerbiViewSet(viewsets.ModelViewSet):
    serializer_class = DerbiSerializer
    queryset = Derbi.objects.all()


class GoalShootsViewSet(viewsets.ModelViewSet):
    serializer_class = GoalShootsSerializer
    queryset = GoalShoots.objects.all()


class GoalkeeperStatsViewSet(viewsets.ModelViewSet):
    serializer_class = GoalkeeperStatsSerializer
    queryset = GoalkeeperStats.objects.all()


class OffenceStatsViewSet(viewsets.ModelViewSet):
    serializer_class = OffenceStatsSerializer
    queryset = OffenceStats.objects.all()

class PersonalEnemyViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalEnemySerializer
    queryset = PersonalEnemy.objects.all()


class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class PlayerInTeamViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerInTeamSerializer
    queryset = PlayerInTeam.objects.all()


class RefereeViewSet(viewsets.ModelViewSet):
    serializer_class = RefereeSerializer
    queryset = Referee.objects.all()


class RefereeInGameViewSet(viewsets.ModelViewSet):
    serializer_class = RefereeInGameSerializer
    queryset = RefereeInGame.objects.all()


class TeamInConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = TeamInConferenceSerializer
    queryset = TeamInConference.objects.all()


class TeamInDivisionViewSet(viewsets.ModelViewSet):
    serializer_class = TeamInDivisionSerializer
    queryset = TeamInDivision.objects.all()


class TeamPenaltiesViewSet(viewsets.ModelViewSet):
    serializer_class = TeamPenaltiesSerializer
    queryset = TeamPenalties.objects.all()


class TeamStatsByPeriodViewSet(viewsets.ModelViewSet):
    serializer_class = TeamStatsByPeriodSerializer
    queryset = TeamStatsByPeriod.objects.all()


class TeamStatsByStrengthViewSet(viewsets.ModelViewSet):
    serializer_class = TeamStatsByStrengthSerializer
    queryset = TeamStatsByStrength.objects.all()


class MannerOfPlayInTeamViewSet(viewsets.ModelViewSet):
    serializer_class = MannerOfPlayInTeamSerializer
    queryset = MannerOfPlayInTeam.objects.all()