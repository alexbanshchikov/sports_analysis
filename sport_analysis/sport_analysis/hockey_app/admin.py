from django.contrib import admin
from .models import PlayerStatus, Amplua, Conference, Division, TimePeriod, Team, GameStats, GameGoals, GamePenalties, \
    MannerOfPlay, TeamAfterGameBullits, Coach, CoachInTeam, Derbi, TeamGoalShoots, GoalkeeperStats, OffenceStats, PersonalEnemy, \
    Player, PlayerInTeam, Referee, RefereeInGame, TeamInConference, TeamInDivision, TeamPenalties, TeamStatsByPeriod, \
    TeamStatsByStrength, MannerOfPlayInTeam

admin.site.register(TeamAfterGameBullits)
admin.site.register(Amplua)
admin.site.register(PlayerStatus)
admin.site.register(Conference)
admin.site.register(Division)
admin.site.register(TimePeriod)
admin.site.register(Team)
admin.site.register(GameStats)
admin.site.register(GameGoals)
admin.site.register(GamePenalties)
admin.site.register(MannerOfPlay)
admin.site.register(Coach)
admin.site.register(CoachInTeam)
admin.site.register(Derbi)
admin.site.register(TeamGoalShoots)
admin.site.register(GoalkeeperStats)
admin.site.register(OffenceStats)
admin.site.register(PersonalEnemy)
admin.site.register(Player)
admin.site.register(PlayerInTeam)
admin.site.register(Referee)
admin.site.register(RefereeInGame)
admin.site.register(TeamInConference)
admin.site.register(TeamInDivision)
admin.site.register(TeamPenalties)
admin.site.register(TeamStatsByPeriod)
admin.site.register(TeamStatsByStrength)
admin.site.register(MannerOfPlayInTeam)

# Register your models here.
