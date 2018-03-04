from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count, Q
from . import team_maker

def index(request):
	context = {
			"players": Player.objects.filter(first_name='Joshua')&Player.objects.filter(all_teams__league_id=3)
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")




# "leagues": League.objects.all(),
# 'teams': Team.objects.all(),
# "players": Player.objects.all()
