from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Miss ZOGHLAMI. J'ai fini les exos du TP donc je fais du python.")

def inscription(request):
    return HttpResponse("Maxime faut rajouter le CSS du bouton inscription")
