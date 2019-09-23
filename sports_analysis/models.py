# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AfterGameBullits(models.Model):
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
    team = models.ForeignKey('Team', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'after_game_bullits'


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
    team1 = models.ForeignKey('Team', models.DO_NOTHING)
    team2 = models.ForeignKey('Team', models.DO_NOTHING)

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
    home_team = models.ForeignKey('Team', models.DO_NOTHING)
    guest_team = models.ForeignKey('Team', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'game'


class GameGoals(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey('Player', models.DO_NOTHING, db_column='author')
    first_assist = models.ForeignKey('Player', models.DO_NOTHING, db_column='first_assist', blank=True, null=True)
    second_assist = models.ForeignKey('Player', models.DO_NOTHING, db_column='second_assist', blank=True, null=True)
    period_number = models.IntegerField()
    time = models.TimeField()
    current_score = models.TextField()
    current_team_strength = models.TextField()
    game = models.ForeignKey(Game, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'game_goals'


class GamePenalties(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.TimeField()
    reason = models.TextField()
    duration = models.IntegerField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING)

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
    attack_time = models.TimeField()
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

    class Meta:
        managed = False
        db_table = 'game_stats'


class GoalShoots(models.Model):
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
    team = models.ForeignKey('Team', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'goal_shoots'


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
    playing_time = models.TimeField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goalkeeper_stats'


class MannerOfPlay(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'manner_of_play'


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
    average_playing_time = models.TimeField()
    average_change_count_per_game = models.DecimalField(max_digits=65535, decimal_places=65535)
    body_contact_count = models.IntegerField()
    blocked_shoot_count = models.IntegerField()
    foul_against_count = models.IntegerField()
    player = models.ForeignKey('Player', models.DO_NOTHING)
    game = models.ForeignKey(Game, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'offence_stats'


class PersonalEnemy(models.Model):
    id = models.BigAutoField(primary_key=True)
    player = models.ForeignKey('Player', models.DO_NOTHING)
    enemy = models.ForeignKey('Player', models.DO_NOTHING)

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


class Team(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    last_game_date = models.DateTimeField()
    games_count = models.IntegerField()
    win_count = models.IntegerField()
    overtime_wins_count = models.IntegerField()
    lose_count = models.IntegerField()
    overtime_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    shutout_games_count = models.IntegerField()
    goalless_games_count = models.IntegerField()
    bullit_wins_count = models.IntegerField()
    bullit_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    score_count = models.IntegerField()
    goals_count = models.IntegerField()
    miss_goals_count = models.IntegerField()
    penalty_time = models.IntegerField()
    penalty_time_against = models.IntegerField()
    empty_net_goals_count = models.IntegerField()
    penalty_bullits_count = models.IntegerField()
    average_goals_count = models.IntegerField()
    attack_time = models.TimeField()
    period_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    shoot_wins_by_period_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    shoot_against_count = models.IntegerField()
    home_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    guest_wins_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    games_with_goalkeeper_pulled_percent = models.DecimalField(max_digits=65535, decimal_places=65535)
    team_manner = models.ForeignKey(MannerOfPlay, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team'


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

    class Meta:
        managed = False
        db_table = 'team_penalties'


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

    class Meta:
        managed = False
        db_table = 'team_stats_by_strength'


class TimePeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'time_period'
