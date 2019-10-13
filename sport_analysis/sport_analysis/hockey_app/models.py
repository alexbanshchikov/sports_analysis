# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amplua(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'amplua'


class Coach(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    date_of_birth = models.DateField()

    class Meta:
        managed = False
        db_table = 'coach'


class CoachInTeam(models.Model):
    coach = models.ForeignKey(Coach, models.DO_NOTHING, primary_key=True)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    games_count = models.IntegerField()
    videoreview_count = models.IntegerField()
    videoreview_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    date_in = models.DateField()
    date_out = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coach_in_team'
        unique_together = (('coach', 'team'), ('coach', 'team'),)


class Conference(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'conference'


class Derbi(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    team1 = models.ForeignKey('Team', models.DO_NOTHING, related_name='team1_foreign_key')
    team2 = models.ForeignKey('Team', models.DO_NOTHING, related_name='team2_foreign_key')

    class Meta:
        managed = False
        db_table = 'derbi'


class Division(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'division'


class Game(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    link = models.TextField()
    home_team = models.ForeignKey('Team', models.DO_NOTHING, related_name='home_team_foreign_key')
    guest_team = models.ForeignKey('Team', models.DO_NOTHING, related_name='guest_team_foreign_key')
    season = models.ForeignKey('Season', models.DO_NOTHING, related_name='season_foreign_key')

    class Meta:
        managed = False
        db_table = 'game'


class GameGoals(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('Player', models.DO_NOTHING, db_column='author', related_name='author_foreign_key')
    first_assist = models.ForeignKey('Player', models.DO_NOTHING, db_column='first_assist', blank=True, null=True, related_name='first_assist_foreign_key')
    second_assist = models.ForeignKey('Player', models.DO_NOTHING, db_column='second_assist', blank=True, null=True, related_name='second_assist_foreign_key')
    time_period = models.ForeignKey('TimePeriod', models.DO_NOTHING, db_column='time_period_id', related_name='time_period_foreign_key')
    current_score = models.TextField()
    current_team_strength = models.TextField()
    game = models.ForeignKey(Game, models.DO_NOTHING)
    time = models.TextField()

    class Meta:
        managed = False
        db_table = 'game_goals'


class GamePenalties(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason = models.TextField()
    duration = models.IntegerField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    time = models.TextField()

    class Meta:
        managed = False
        db_table = 'game_penalties'


class GameStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    goals_count = models.IntegerField()
    shoots_count = models.IntegerField()
    implemented_goal_shoot_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    blocked_shots_count = models.IntegerField()
    body_contact_count = models.IntegerField()
    powerplay_goals_count = models.IntegerField()
    shorthanded_goals_count = models.IntegerField()
    powerplay_count = models.IntegerField()
    faceoff_wins_count = models.IntegerField()
    penalty_time = models.TimeField()
    distance = models.DecimalField(max_digits=65535, decimal_places=65535)
    puck_owned_time = models.TimeField()
    team = models.ForeignKey('Team', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING)
    time_period = models.ForeignKey('TimePeriod', models.DO_NOTHING)
    attack_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'game_stats'


class GoalkeeperStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    games_count = models.IntegerField()
    win_count = models.IntegerField()
    defeat_count = models.IntegerField()
    bullit_count = models.IntegerField()
    shoots_count = models.IntegerField()
    missed_pucks_count = models.IntegerField()
    reflected_pucks_count = models.IntegerField()
    reflected_pucks_count_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    reliability_factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    goals_count = models.IntegerField()
    assists_count = models.IntegerField()
    shutouts_count = models.IntegerField()
    penalty_time = models.IntegerField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING, blank=True, null=True)
    season = models.ForeignKey('Season', models.DO_NOTHING)
    playing_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'goalkeeper_stats'


class League(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'league'


class MannerOfPlay(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'manner_of_play'


class MannerOfPlayInTeam(models.Model):
    team = models.ForeignKey('Team', models.DO_NOTHING, primary_key=True)
    manner_of_play = models.ForeignKey(MannerOfPlay, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'manner_of_play_in_team'
        unique_together = (('team', 'manner_of_play'), ('team', 'manner_of_play'),)


class OffenceStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    games_count = models.IntegerField()
    goals_count = models.IntegerField()
    assists_count = models.IntegerField()
    scores_count = models.IntegerField()
    plus_minus = models.IntegerField()
    plus = models.IntegerField()
    minus = models.IntegerField()
    penalty_time = models.IntegerField()
    even_strengh_goals_count = models.IntegerField()
    powerplay_goals_count = models.IntegerField()
    shorthanded_goals_count = models.IntegerField()
    overtime_goals_count = models.IntegerField()
    winning_goals_count = models.IntegerField()
    final_bullits_count = models.IntegerField()
    goal_shoot_count = models.IntegerField()
    score_goals_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    implemented_goal_shoot_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    average_shoot_count_per_game = models.DecimalField(max_digits=65535, decimal_places=65535)
    faceoff_count = models.IntegerField()
    win_faceoff_count = models.IntegerField()
    win_faceoff_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    average_change_count_per_game = models.DecimalField(max_digits=65535, decimal_places=65535)
    body_contact_count = models.IntegerField()
    blocked_shoot_count = models.IntegerField()
    foul_against_count = models.IntegerField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING, blank=True, null=True)
    season = models.ForeignKey('Season', models.DO_NOTHING)
    average_playing_time = models.TextField()

    class Meta:
        managed = False
        db_table = 'offence_stats'


class PersonalEnemy(models.Model):
    id = models.BigAutoField(primary_key=True)
    player = models.ForeignKey('Player', models.DO_NOTHING, related_name='player_foreign_key')
    enemy = models.ForeignKey('Player', models.DO_NOTHING, related_name='enemy_foreign_key')

    class Meta:
        managed = False
        db_table = 'personal_enemy'


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    number = models.IntegerField()
    date_of_birth = models.DateField()
    amplua = models.ForeignKey(Amplua, models.DO_NOTHING)
    status = models.ForeignKey('PlayerStatus', models.DO_NOTHING)
    nationality = models.TextField()
    date_of_contract_expiration = models.DateField()

    class Meta:
        managed = False
        db_table = 'player'


class PlayerInTeam(models.Model):
    player = models.ForeignKey(Player, models.DO_NOTHING, primary_key=True)
    team = models.ForeignKey('Team', models.DO_NOTHING)
    date_in = models.DateField()
    date_out = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_in_team'
        unique_together = (('player', 'team'), ('player', 'team'),)


class PlayerStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'player_status'


class Referee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    penalty_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'referee'


class RefereeInGame(models.Model):
    referee = models.ForeignKey(Referee, models.DO_NOTHING, primary_key=True)
    game = models.ForeignKey(Game, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'referee_in_game'
        unique_together = (('referee', 'game'), ('referee', 'game'),)


class Season(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'season'


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    last_game_date = models.DateField(blank=True, null=True)
    logo = models.TextField(blank=True, null=True)
    league = models.ForeignKey(League, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team'


class TeamAdditionalStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    overtime_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    bullit_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    empty_net_goals_count = models.IntegerField()
    penalty_bullits_count = models.IntegerField()
    average_goals_count = models.DecimalField(max_digits=65535, decimal_places=65535)
    attack_time = models.TextField()
    period_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    shoot_wins_by_period_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    shoot_against_count = models.IntegerField()
    home_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    guest_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    games_with_goalkeeper_pulled_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_additional_stats'


class TeamAfterGameBullits(models.Model):
    id = models.BigAutoField(primary_key=True)
    bullits_games_count = models.IntegerField()
    wins_count = models.IntegerField()
    lose_count = models.IntegerField()
    bullits_shoot_count = models.IntegerField()
    bullits_goals_count = models.IntegerField()
    bullits_goals_count_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    against_bullits_shoot_count = models.IntegerField()
    against_bullits_goals_count = models.IntegerField()
    against_bullits_goals_count_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_after_game_bullits'


class TeamGoalShoots(models.Model):
    id = models.BigAutoField(primary_key=True)
    home_goal_shoots_count = models.IntegerField()
    home_implemented_goal_shoots_count = models.IntegerField()
    home_implemented_goal_shoots_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    guest_goal_shoots_count = models.IntegerField()
    guest_implemented_goal_shoots_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    guest_implemented_goal_shoots_count = models.IntegerField()
    total_goal_shoots_count = models.IntegerField()
    total_implemented_goal_shoots_count = models.IntegerField()
    total_implemented_goal_shoots_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_goal_shoots'


class TeamInConference(models.Model):
    team = models.ForeignKey(Team, models.DO_NOTHING, primary_key=True)
    conference = models.ForeignKey(Conference, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_in_conference'
        unique_together = (('team', 'conference'), ('team', 'conference'),)


class TeamInDivision(models.Model):
    team = models.ForeignKey(Team, models.DO_NOTHING, primary_key=True)
    division = models.ForeignKey(Division, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_in_division'
        unique_together = (('team', 'division'),)


class TeamMainStats(models.Model):
    id = models.BigAutoField(primary_key=True)
    games_count = models.IntegerField()
    win_count = models.IntegerField()
    overtime_wins_count = models.IntegerField()
    lose_count = models.IntegerField()
    shutout_games_count = models.IntegerField()
    goalless_games_count = models.IntegerField()
    bullit_wins_count = models.IntegerField()
    score_count = models.IntegerField()
    goals_count = models.IntegerField()
    miss_goals_count = models.IntegerField()
    penalty_time = models.IntegerField()
    penalty_time_against = models.IntegerField()
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)
    type_of_game = models.ForeignKey('TypeOfGame', models.DO_NOTHING)
    bullit_lose_count = models.IntegerField()
    overtime_lose_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'team_main_stats'


class TeamPenalties(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_2_minutes_penalty_count = models.IntegerField(db_column='2_minutes_penalty_count')  # Field renamed because it wasn't a valid Python identifier.
    number_5_minutes_penalty_count = models.IntegerField(db_column='5_minutes_penalty_count')  # Field renamed because it wasn't a valid Python identifier.
    number_10_minutes_penalty_count = models.IntegerField(db_column='10_minutes_penalty_count')  # Field renamed because it wasn't a valid Python identifier.
    number_20_minutes_penalty_count = models.IntegerField(db_column='20_minutes_penalty_count')  # Field renamed because it wasn't a valid Python identifier.
    number_25_minutes_penalty_count = models.IntegerField(db_column='25_minutes_penalty_count')  # Field renamed because it wasn't a valid Python identifier.
    penalty_shoot_count = models.IntegerField()
    team_penalty_time = models.IntegerField()
    goalkeeper_penalty_time = models.IntegerField()
    total_penalty_time = models.IntegerField()
    average_penalty_time_per_game = models.DecimalField(max_digits=65535, decimal_places=65535)
    against_total_penalty_time = models.IntegerField()
    against_average_penalty_time_per_game = models.DecimalField(max_digits=65535, decimal_places=65535)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_penalties'


class TeamStatsByImplementedGoals(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_5x5_goals_count = models.IntegerField(db_column='5x5_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_5x4_goals_count = models.IntegerField(db_column='5x4_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_5x3_goals_count = models.IntegerField(db_column='5x3_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_4x4_goals_count = models.IntegerField(db_column='4x4_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_4x3_goals_count = models.IntegerField(db_column='4x3_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_3x3_goals_count = models.IntegerField(db_column='3x3_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_3x4_goals_count = models.IntegerField(db_column='3x4_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_3x5_goals_count = models.IntegerField(db_column='3x5_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    number_4x5_goals_count = models.IntegerField(db_column='4x5_goals_count')  # Field renamed because it wasn't a valid Python identifier.
    empty_net_goals_count = models.IntegerField()
    bullit_goals_count = models.IntegerField()
    total_goals_count = models.IntegerField()
    average_goals_count_per_game = models.DecimalField(max_digits=65535, decimal_places=65535)
    game = models.ForeignKey(Game, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_stats_by_implemented_goals'


class TeamStatsByMissedGoals(models.Model):
    id = models.BigAutoField(primary_key=True)
    number_5x5_miss_count = models.IntegerField(db_column='5x5_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_5x4_miss_count = models.IntegerField(db_column='5x4_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_5x3_miss_count = models.IntegerField(db_column='5x3_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_4x4_miss_count = models.IntegerField(db_column='4x4_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_4x3_miss_count = models.IntegerField(db_column='4x3_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_3x3_miss_count = models.IntegerField(db_column='3x3_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_3x4_miss_count = models.IntegerField(db_column='3x4_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_3x5_miss_count = models.IntegerField(db_column='3x5_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    number_4x5_miss_count = models.IntegerField(db_column='4x5_miss_count')  # Field renamed because it wasn't a valid Python identifier.
    empty_net_miss_count = models.IntegerField()
    bullit_miss_count = models.IntegerField()
    total_miss_count = models.IntegerField()
    average_miss_count_per_game = models.DecimalField(max_digits=65535, decimal_places=65535)
    game = models.ForeignKey(Game, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_stats_by_missed_goals'


class TeamStatsByPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    win_period_count = models.IntegerField()
    draw_period_count = models.IntegerField()
    lose_period_count = models.IntegerField()
    score_count = models.IntegerField()
    games_without_goals_count = models.IntegerField()
    shutout_games_count = models.IntegerField()
    goals_count = models.IntegerField()
    missed_count = models.IntegerField()
    penalty_time = models.IntegerField()
    against_penalty_time = models.IntegerField()
    time_period = models.ForeignKey('TimePeriod', models.DO_NOTHING)
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_stats_by_period'


class TeamStatsByStrength(models.Model):
    id = models.BigAutoField(primary_key=True)
    powerplays_count = models.IntegerField()
    powerplay_goals_count = models.IntegerField()
    implemented_powerplays_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    missed_goals_powerplays_count = models.IntegerField()
    shorthanded_count = models.IntegerField()
    shorthanded_goals_count = models.IntegerField()
    implemented_shorthanded_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    missed_goals_shorthanded_count = models.IntegerField()
    team = models.ForeignKey(Team, models.DO_NOTHING)
    season = models.ForeignKey(Season, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_stats_by_strength'


class TimePeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'time_period'


class TypeOfGame(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'type_of_game'
