from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def home_view(request):
	 return HttpResponse("Hello!") 

def Start(request):
	return render(request, "Start.html")

def StronaGlowna(request):
	return render(request, "StronaGlowna.html")

def zakladanie_konta(request):
	return render(request, "zakladanie_konta.html")

def Statystyki(request):
	return render(request, "Statystyki.html")

def Roczniki(request):
	return render(request, "Roczniki.html")

def Regulamin(request):
	return render(request, "Regulamin.html")

def Projekt(request):
	return render(request, "Projekt.html")

def Omnie(request):
	return render(request, "Omnie.html")

def Kontakt(request):
	return render(request, "Kontakt.html")

def P_2020(request):
	return render(request, "2020.html")

def P_2019(request):
	return render(request, "2019.html")

	
def P_2018(request):
	return render(request, "2018.html")

