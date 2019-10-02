from rest_framework import serializers
from .models import PlayerStatus, Amplua, Conference, Division, TimePeriod, Team, GameStats, Game, GameGoals, \
    GamePenalties, MannerOfPlay, AfterGameBullits, Coach, CoachInTeam, Derbi, GoalShoots, GoalkeeperStats, OffenceStats, \
    PersonalEnemy, Player, PlayerInTeam, Referee, RefereeInGame, TeamInConference, TeamInDivision, TeamPenalties, \
    TeamStatsByPeriod, TeamStatsByStrength, MannerOfPlayInTeam


class PlayerStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStatus
        fields = ('id', 'name')


class AmpluaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amplua
        fields = ('id', 'name')


class AfterGameBullitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfterGameBullits
        fields = ('id', 'bullits_games_count', 'wins_count', 'lose_count', 'bullits_shoot_count',
                  'bullits_goals_count', 'bullits_goals_count_percent', 'against_bullits_shoot_count',
                  'against_bullits_goals_count', 'against_bullits_goals_count_percent', 'team')


class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ('id', 'name', 'date_of_birth')


class CoachInTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachInTeam
        fields = ('coach', 'team', 'games_count', 'videoreview_count', 'videoreview_percent', 'date_in', 'date_out')


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = ('id', 'name')


class DerbiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Derbi
        fields = ('id', 'name', 'team1', 'team2')


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ('id', 'name')


class TimePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimePeriod
        fields = ('id', 'name')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'last_game_date', 'games_count', 'win_count', 'overtime_wins_count',
                  'lose_count', 'overtime_wins_percent', 'shutout_games_count', 'goalless_games_count',
                  'bullit_wins_count', 'bullit_wins_percent', 'score_count', 'goals_count',
                  'miss_goals_count', 'penalty_time', 'penalty_time_against', 'empty_net_goals_count',
                  'penalty_bullits_count', 'average_goals_count', 'attack_time', 'period_wins_percent',
                  'shoot_wins_by_period_percent', 'shoot_against_count', 'home_wins_percent',
                  'guest_wins_percent', 'games_with_goalkeeper_pulled_percent')


class GameStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameStats
        fields = ('id', 'goals_count', 'shoots_count', 'implemented_goal_shoot_percent', 'blocked_shots_count',
                  'body_contact_count', 'attack_time', 'powerplay_goals_count', 'shorthanded_goals_count',
                  'powerplay_count', 'faceoff_wins_count', 'penalty_time', 'distance', 'puck_owned_time',
                  'team', 'game', 'time_period')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'date', 'link', 'home_team', 'guest_team')


class GameGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameGoals
        fields = ('id', 'author', 'first_assist', 'second_assist', 'time_period', 'time', 'current_score',
                  'current_team_strength', 'game')


class GamePenaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePenalties
        fields = ('id', 'time', 'reason', 'duration', 'player', 'game')


class MannerOfPlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = MannerOfPlay
        fields = ('id', 'name')


class GoalShootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalShoots
        fields = ('id', 'home_goal_shoots_count', 'home_implemented_goal_shoots_count', 'home_implemented_goal_shoots_percent',
                  'guest_goal_shoots_count', 'guest_implemented_goal_shoots_percent', 'guest_implemented_goal_shoots_count',
                  'total_goal_shoots_count', 'total_implemented_goal_shoots_count', 'total_implemented_goal_shoots_percent',
                  'team')


class GoalkeeperStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoalkeeperStats
        fields = ('id', 'games_count', 'win_count', 'defeat_count', 'bullit_count', 'shoots_count', 'missed_pucks_count',
                  'reflected_pucks_count', 'reflected_pucks_count_percent', 'reliability_factor', 'goals_count',
                  'assists_count', 'shutouts_count', 'penalty_time', 'playing_time', 'player', 'game')


class OffenceStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffenceStats
        fields = ('id', 'games_count', 'goals_count', 'assists_count', 'scores_count', 'plus_minus', 'plus',
                  'minus', 'penalty_time', 'even_strengh_goals_count', 'powerplay_goals_count',
                  'shorthanded_goals_count', 'overtime_goals_count', 'winning_goals_count', 'final_bullits_count',
                  'goal_shoot_count', 'score_goals_percent', 'implemented_goal_shoot_percent', 'average_shoot_count_per_game',
                  'faceoff_count', 'win_faceoff_count', 'win_faceoff_percent', 'average_playing_time', 'average_change_count_per_game',
                  'body_contact_count', 'blocked_shoot_count', 'foul_against_count', 'player', 'game')


class PersonalEnemySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalEnemy
        fields = ('id', 'player', 'enemy')


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name', 'number', 'date_of_birth', 'amplua', 'status')


class PlayerInTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInTeam
        fields = ('player', 'team', 'date_in', 'date_out')


class RefereeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ('id', 'name', 'penalty_count')


class RefereeInGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = RefereeInGame
        fields = ('referee', 'game')


class TeamInConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInConference
        fields = ('team', 'conference')


class TeamInDivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamInDivision
        fields = ('team', 'division')


class TeamPenaltiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamPenalties
        fields = ('id', 'number_2_minutes_penalty_count', 'number_5_minutes_penalty_count', 'number_10_minutes_penalty_count',
                  'number_20_minutes_penalty_count', 'number_25_minutes_penalty_count', 'penalty_shoot_count',
                  'team_penalty_time', 'goalkeeper_penalty_time', 'total_penalty_time', 'average_penalty_time_per_game',
                  'against_total_penalty_time', 'against_average_penalty_time_per_game', 'team')


class TeamStatsByPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStatsByPeriod
        fields = ('id', 'win_period_count', 'draw_period_count', 'lose_period_count', 'score_count',
                  'games_without_goals_count', 'shutout_games_count', 'goals_count', 'missed_count',
                  'penalty_time', 'against_penalty_time', 'time_period', 'team')


class TeamStatsByStrengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamStatsByStrength
        fields = ('id', 'powerplays_count', 'powerplay_goals_count', 'implemented_powerplays_percent',
                  'missed_goals_powerplays_count', 'shorthanded_count', 'shorthanded_goals_count',
                  'implemented_shorthanded_percent', 'missed_goals_shorthanded_count',
                  'number_5x5_goals_count', 'number_5x4_goals_count', 'number_5x3_goals_count', 'number_4x4_goals_count',
                  'number_4x3_goals_count', 'number_3x3_goals_count', 'number_3x4_goals_count', 'number_3x5_goals_count',
                  'number_4x5_goals_count', 'empty_net_goals_count', 'bullit_goals_count', 'total_goals_count',
                  'average_goals_count_per_game', 'number_5x5_miss_count', 'number_5x4_miss_count', 'number_5x3_miss_count',
                  'number_4x4_miss_count', 'number_4x3_miss_count', 'number_3x3_miss_count', 'number_3x4_miss_count',
                  'number_3x5_miss_count', 'number_4x5_miss_count', 'empty_net_miss_count', 'bullit_miss_count',
                  'total_miss_count', 'average_miss_count_per_game', 'game', 'team')


class MannerOfPlayInTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = MannerOfPlayInTeam
        fields = ('team', 'manner_of_play')
