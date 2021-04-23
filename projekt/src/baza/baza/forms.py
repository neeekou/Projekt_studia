from django import forms

from .models import *

class ContactForm(forms.ModelForm):
	class Meta:
		model = Dane_osoba
		fields  = ('imie','nazwisko','haslo','data','email','nr_telefonu','plec','PESEL',)

