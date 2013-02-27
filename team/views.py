# Create your views here.


from team.models import Team, Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    return render(request, "roster/home.html")

def team(request, pk):
    #team = Team.objects.order_by('?')[0]
    team = get_object_or_404(Team, id=pk)
    return render(request, "roster/team.html", {'team': team})

def player(request, pk):
    #player = Player.objects.order_by('?')[0]
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/player.html", {'player': player})

