from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1> This is the sports website")


def detail(request, team_id):
    return HttpResponse("<h2>Details for Team Id: " + str(team_id) + "</h2>")

