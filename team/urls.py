from django.conf.urls.defaults import patterns, url

from team import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='team_home'),
    url(r'^team/(?P<pk>\d+)$', views.team, name= 'team_team'),
    url(r'^player/(?P<pk>\d+)$', views.player, name= 'team_player'), 
    )