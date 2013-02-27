from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(unique=True, max_length=50)
    number = models.CharField(unique=True, max_length=3)
    position = models.CharField(unique=False, max_length=12)
    height = models.CharField(unique=False, max_length=12)
    weight = models.CharField(unique=False, max_length=12)
    year = models.CharField(unique=False, null=True, max_length=3)
    hometown = models.CharField(unique=False, max_length=50)
    high = models.CharField(unique=False, max_length=50)
    major = models.CharField(unique=False, max_length=50)
    bio = models.CharField(unique=True, max_length=900)
    
    class Meta(object):
        ordering = ('name',)
        
    def __unicode__(self):
        return U' %s %s' %(self.name)


class Team(models.Model):
    name = models.CharField(unique=True, max_length=50)
    coach = models.CharField(unique=False, max_length=50)
    season = models.CharField(unique=False, max_length=50)
    players = models.ManyToManyField(Player)

    class Meta(object):
        verbose_name_plural = "Teams"
        ordering = ('name',)
        
    def __unicode__(self):
        return U'%s %s' %(self.name, self.coach)
    
    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        super(Team.self).save(*args, **kwargs)