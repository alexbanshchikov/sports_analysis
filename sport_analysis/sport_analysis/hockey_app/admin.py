from django.contrib import admin
from .models import Amplua, Coach, CoachInTeam, Conference, Derbi, Division, Game, GameGoals, GamePenalties, \
    GameStatsByBodyContact, GameStatsByDifferentStrength, GameStatsByGoalShoots, GameStatsSummary, GoalkeeperStats, \
    League, MannerOfPlay, MannerOfPlayInTeam, OffenceStats, PersonalEnemy, Player, \
    PlayerInTeam, PlayerStatus, Referee, RefereeInGame, Season, Team, TeamAdditionalStats, TeamAfterGameBullits, \
    TeamGoalShoots, TeamInConference, TeamInDivision, TeamMainStats, TeamPenalties, TeamStatsByImplementedGoals, \
    TeamStatsByMissedGoals, TeamStatsByPeriod, TeamStatsByStrength, TimePeriod, TypeOfGame

admin.site.register(Amplua)

admin.site.register(Coach)
admin.site.register(CoachInTeam)

admin.site.register(Conference)

admin.site.register(Derbi)

admin.site.register(Division)

admin.site.register(Game)
admin.site.register(GameGoals)
admin.site.register(GamePenalties)
admin.site.register(GameStatsByBodyContact)
admin.site.register(GameStatsByDifferentStrength)
admin.site.register(GameStatsByGoalShoots)
admin.site.register(GameStatsSummary)

admin.site.register(GoalkeeperStats)

admin.site.register(League)

admin.site.register(MannerOfPlay)
admin.site.register(MannerOfPlayInTeam)

admin.site.register(OffenceStats)

admin.site.register(PersonalEnemy)

admin.site.register(Player)
admin.site.register(PlayerInTeam)
admin.site.register(PlayerStatus)

admin.site.register(Referee)
admin.site.register(RefereeInGame)

admin.site.register(Season)

admin.site.register(Team)
admin.site.register(TeamAdditionalStats)
admin.site.register(TeamAfterGameBullits)
admin.site.register(TeamGoalShoots)
admin.site.register(TeamInConference)
admin.site.register(TeamInDivision)
admin.site.register(TeamMainStats)
admin.site.register(TeamPenalties)
admin.site.register(TeamStatsByImplementedGoals)
admin.site.register(TeamStatsByMissedGoals)
admin.site.register(TeamStatsByPeriod)
admin.site.register(TeamStatsByStrength)

admin.site.register(TimePeriod)

admin.site.register(TypeOfGame)

# Register your models here.
