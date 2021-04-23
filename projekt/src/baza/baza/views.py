from django.shortcuts import render
from .models import Ustawy
from .models import Dane_osoba
from django.http import HttpResponse

from .forms import Dane_osoba

def home_view(request):
	 return HttpResponse("Hello!") 

def Start(request):
	return render(request, "Start.html")

def StronaGlowna(request):
	return render(request, "StronaGlowna.html")

def zakladanie_konta(request):
	results=Dane_osoba.objects.all()
	return render(request, "zakladanie_konta.html",{"data":results})

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

def P_2021(request):
	results=Ustawy.objects.all()
	return render(request, "2021.html",{"data":results})

def P_2020(request):
	results=Ustawy.objects.all()
	return render(request, "2020.html",{"data":results})

def P_2019(request):
	results=Ustawy.objects.all()
	return render(request, "2019.html",{"data":results})

	
def P_2018(request):
	results=Ustawy.objects.all()
	return render(request, "2018.html",{"data":results})

def P_2017(request):
	results=Ustawy.objects.all()
	return render(request, "2017.html",{"data":results})

def P_2016(request):
	results=Ustawy.objects.all()
	return render(request, "2016.html",{"data":results})

def P_2015(request):
	results=Ustawy.objects.all()
	return render(request, "2015.html",{"data":results})

def P_2014(request):
	results=Ustawy.objects.all()
	return render(request, "2014.html",{"data":results})

def P_2013(request):
	results=Ustawy.objects.all()
	return render(request, "2013.html",{"data":results})

def base(request):
	form = Dane_osoba()
	return render(request, "base.html",{"form":form})

def post_new(request):
    form = Dane_osoba()
    return render(request, 'base.html', {'form': form})

#def main_base(request):
#	return render(request, "main_base.html")

#def main_base_page(request):
#	return render(request, "main_base_page.html")