# Create your views here.


from team.models import Team, Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    
       return render(request, "roster/home.html")

def team(request, pk):
    #team = Team.objects.order_by('?')[0]
    team = get_object_or_404(Team, id=pk)
    
    tempTeam = Team.objects.get(id=pk)
    teamList = tempTeam.players.all()
    htmlVar = ""
    for i in teamList:
       htmlVar += "<tr><td>" + str(i.number) + "</td><td>" + "<a href='{% url 'team_players' i.id %}'>" + i.name + "</a></td><td>" + i.last + "</td><td>" + i.position + "</td><td>" + i.height + "</td><td>" + i.weight + "</td><td>" + i.year + "</td></tr>"
    
        
    context = {
        'teamList': teamList,
        'team': team,
        'htmlVar': htmlVar,
    }
    
    
    return render(request, "roster/team.html", context)

def player(request, pk):
    #player = Player.objects.order_by('?')[0]
    player = get_object_or_404(Player, id=pk)
    return render(request, "roster/player.html", {'player': player})
 
def teamList(request):
    
    return render (request, "roster/team.html")