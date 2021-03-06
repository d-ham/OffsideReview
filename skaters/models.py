from django.db import models


class Skaters(models.Model):
    
    player = models.CharField(max_length=30, default='')
    player_id = models.CharField(max_length=7, default='')
    position = models.CharField(max_length=3, default='', null=True)
    handedness = models.CharField(max_length=2, default='', null=True)
    season = models.IntegerField(null=True)
    game_id = models.IntegerField(null=True)
    date = models.DateField(null=True)
    team = models.CharField(max_length=3, default='', null=True)
    opponent = models.CharField(max_length=3, default='', null=True)
    home = models.CharField(max_length=3, default='', null=True)
    strength = models.CharField(max_length=3, default='', null=True)
    toi_on = models.IntegerField(null=True)
    goals = models.IntegerField(null=True)
    a1 = models.IntegerField(null=True)
    a2 = models.IntegerField(null=True)
    isf = models.IntegerField(null=True)
    ifen = models.IntegerField(null=True)
    ixg = models.FloatField(null=True)
    icors = models.IntegerField(null=True)
    iblocks = models.IntegerField(null=True)
    pen_drawn = models.IntegerField(null=True)
    pen_taken = models.IntegerField(null=True)
    gives = models.IntegerField(null=True)
    takes = models.IntegerField(null=True)
    hits_f = models.IntegerField(null=True)
    hits_a = models.IntegerField(null=True)
    ifac_win = models.IntegerField(null=True)
    ifac_loss = models.IntegerField(null=True)
    shots_f = models.IntegerField(null=True)
    goals_f = models.IntegerField(null=True)
    fenwick_f = models.IntegerField(null=True)
    xg_f = models.FloatField(null=True)
    corsi_f = models.IntegerField(null=True)
    shots_a = models.IntegerField(null=True)
    goals_a = models.IntegerField(null=True)
    fenwick_a = models.IntegerField(null=True)
    xg_a = models.FloatField(null=True)
    corsi_a = models.IntegerField(null=True)
    shots_f_sa = models.FloatField(null=True)
    fenwick_f_sa = models.FloatField(null=True)
    corsi_f_sa = models.FloatField(null=True)
    shots_a_sa = models.FloatField(null=True)
    fenwick_a_sa = models.FloatField(null=True)
    corsi_a_sa = models.FloatField(null=True)
    face_off = models.IntegerField(null=True)
    face_def = models.IntegerField(null=True)
    face_neu = models.IntegerField(null=True)
    toi_off = models.IntegerField(null=True)
    shots_f_off = models.IntegerField(null=True)
    goals_f_off = models.IntegerField(null=True)
    fenwick_f_off = models.IntegerField(null=True)
    xg_f_off = models.FloatField(null=True)
    corsi_f_off = models.IntegerField(null=True)
    shots_a_off = models.IntegerField(null=True)
    goals_a_off = models.IntegerField(null=True)
    fenwick_a_off = models.IntegerField(null=True)
    xg_a_off = models.FloatField(null=True)
    corsi_a_off = models.IntegerField(null=True)
    shots_f_off_sa = models.FloatField(null=True)
    fenwick_f_off_sa = models.FloatField(null=True)
    corsi_f_off_sa = models.FloatField(null=True)
    shots_a_off_sa = models.FloatField(null=True)
    fenwick_a_off_sa = models.FloatField(null=True)
    corsi_a_off_sa = models.FloatField(null=True)
    face_off_off = models.IntegerField(null=True)
    face_neu_off = models.IntegerField(null=True)
    face_def_off = models.IntegerField(null=True)
    if_empty = models.IntegerField(null=True)
    primary_key = models.CharField(max_length=100, primary_key=True, default='')
    shooter_xg_a = models.FloatField(null=True)
    shooter_xg_a_off = models.FloatField(null=True)
    shooter_xg_f = models.FloatField(null=True)
    shooter_xg_f_off = models.FloatField(null=True)
    shooter_ixg = models.FloatField(null=True)

    def __str__(self):
        return self.player


        
        


