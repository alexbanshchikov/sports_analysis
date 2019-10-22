from django.shortcuts import render

from rest_framework import viewsets

from .serializers import AmpluaSerializer, CoachSerializer, CoachInTeamSerializer, ConferenceSerializer, \
    DerbiSerializer, DivisionSerializer, GameSerializer, GameGoalsSerializer, GamePenaltiesSerializer, \
    GameStatsByBodyContactSerializer, GameStatsByDifferentStrengthSerializer, GameStatsByGoalShootsSerializer, \
    GameStatsSummarySerializer, GoalkeeperStatsSerializer, LeagueSerializer, MannerOfPlaySerializer, \
    MannerOfPlayInTeamSerializer, OffenceStatsSerializer, PersonalEnemySerializer, PlayerSerializer, \
    PlayerInTeamSerializer, PlayerStatusSerializer, RefereeSerializer, RefereeInGameSerializer, \
    SeasonSerializer, TeamSerializer, TeamAdditionalStatsSerializer, TeamAfterGameBullitsSerializer, \
    TeamGoalShootsSerializer, TeamInConferenceSerializer, TeamInDivisionSerializer, TeamMainStatsSerializer, \
    TeamPenaltiesSerializer, TeamStatsByImplementedGoalsSerializer, TeamStatsByMissedGoalsSerializer, \
    TeamStatsByPeriodSerializer, TeamStatsByStrengthSerializer, TimePeriodSerializer, TypeOfGameSerializer

from .models import Amplua, Coach, CoachInTeam, Conference, Derbi, Division, Game, GameGoals, GamePenalties, \
    GameStatsByBodyContact, GameStatsByDifferentStrength, GameStatsByGoalShoots, GameStatsSummary, GoalkeeperStats, \
    League, MannerOfPlay, MannerOfPlayInTeam, OffenceStats, PersonalEnemy, Player, \
    PlayerInTeam, PlayerStatus, Referee, RefereeInGame, Season, Team, TeamAdditionalStats, TeamAfterGameBullits, \
    TeamGoalShoots, TeamInConference, TeamInDivision, TeamMainStats, TeamPenalties, TeamStatsByImplementedGoals, \
    TeamStatsByMissedGoals, TeamStatsByPeriod, TeamStatsByStrength, TimePeriod, TypeOfGame


class AmpluaViewSet(viewsets.ModelViewSet):
    serializer_class = AmpluaSerializer
    queryset = Amplua.objects.all()


class CoachViewSet(viewsets.ModelViewSet):
    serializer_class = CoachSerializer
    queryset = Coach.objects.all()


class CoachInTeamViewSet(viewsets.ModelViewSet):
    serializer_class = CoachInTeamSerializer
    queryset = CoachInTeam.objects.all()


class ConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ConferenceSerializer
    queryset = Conference.objects.all()


class DerbiViewSet(viewsets.ModelViewSet):
    serializer_class = DerbiSerializer
    queryset = Derbi.objects.all()


class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer
    queryset = Division.objects.all()


class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()


class GameGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = GameGoalsSerializer
    queryset = GameGoals.objects.all()


class GamePenaltiesViewSet(viewsets.ModelViewSet):
    serializer_class = GamePenaltiesSerializer
    queryset = GamePenalties.objects.all()


class GameStatsByBodyContactViewSet(viewsets.ModelViewSet):
    serializer_class = GameStatsByBodyContactSerializer
    queryset = GameStatsByBodyContact.objects.all()


class GameStatsByDifferentStrengthViewSet(viewsets.ModelViewSet):
    serializer_class = GameStatsByDifferentStrengthSerializer
    queryset = GameStatsByDifferentStrength.objects.all()


class GameStatsByGoalShootsViewSet(viewsets.ModelViewSet):
    serializer_class = GameStatsByGoalShootsSerializer
    queryset = GameStatsByGoalShoots.objects.all()


class GameStatsSummaryViewSet(viewsets.ModelViewSet):
    serializer_class = GameStatsSummarySerializer
    queryset = GameStatsSummary.objects.all()


class GoalkeeperStatsViewSet(viewsets.ModelViewSet):
    serializer_class = GoalkeeperStatsSerializer
    queryset = GoalkeeperStats.objects.all()


class LeagueViewSet(viewsets.ModelViewSet):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()


class MannerOfPlayViewSet(viewsets.ModelViewSet):
    serializer_class = MannerOfPlaySerializer
    queryset = MannerOfPlay.objects.all()


class MannerOfPlayInTeamViewSet(viewsets.ModelViewSet):
    serializer_class = MannerOfPlayInTeamSerializer
    queryset = MannerOfPlayInTeam.objects.all()


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


class PlayerStatusViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerStatusSerializer
    queryset = PlayerStatus.objects.all()


class RefereeViewSet(viewsets.ModelViewSet):
    serializer_class = RefereeSerializer
    queryset = Referee.objects.all()


class RefereeInGameViewSet(viewsets.ModelViewSet):
    serializer_class = RefereeInGameSerializer
    queryset = RefereeInGame.objects.all()


class SeasonViewSet(viewsets.ModelViewSet):
    serializer_class = SeasonSerializer
    queryset = Season.objects.all()


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()


class TeamAdditionalStatsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamAdditionalStatsSerializer
    queryset = TeamAdditionalStats.objects.all()


class TeamAfterGameBullitsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamAfterGameBullitsSerializer
    queryset = TeamAfterGameBullits.objects.all()


class TeamGoalShootsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamGoalShootsSerializer
    queryset = TeamGoalShoots.objects.all()


class TeamInConferenceViewSet(viewsets.ModelViewSet):
    serializer_class = TeamInConferenceSerializer
    queryset = TeamInConference.objects.all()


class TeamInDivisionViewSet(viewsets.ModelViewSet):
    serializer_class = TeamInDivisionSerializer
    queryset = TeamInDivision.objects.all()


class TeamMainStatsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMainStatsSerializer
    queryset = TeamMainStats.objects.all()


class TeamPenaltiesViewSet(viewsets.ModelViewSet):
    serializer_class = TeamPenaltiesSerializer
    queryset = TeamPenalties.objects.all()


class TeamStatsByImplementedGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamStatsByImplementedGoalsSerializer
    queryset = TeamStatsByImplementedGoals.objects.all()


class TeamStatsByMissedGoalsViewSet(viewsets.ModelViewSet):
    serializer_class = TeamStatsByMissedGoalsSerializer
    queryset = TeamStatsByMissedGoals.objects.all()


class TeamStatsByPeriodViewSet(viewsets.ModelViewSet):
    serializer_class = TeamStatsByPeriodSerializer
    queryset = TeamStatsByPeriod.objects.all()


class TeamStatsByStrengthViewSet(viewsets.ModelViewSet):
    serializer_class = TeamStatsByStrengthSerializer
    queryset = TeamStatsByStrength.objects.all()


class TimePeriodViewSet(viewsets.ModelViewSet):
    serializer_class = TimePeriodSerializer
    queryset = TimePeriod.objects.all()


class TypeOfGameViewSet(viewsets.ModelViewSet):
    serializer_class = TypeOfGameSerializer
    queryset = TypeOfGame.objects.all()
