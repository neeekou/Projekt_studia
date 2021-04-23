from django.db import models

class Ustawy(models.Model):
	index=models.IntegerField(primary_key=True)
	rok=models.IntegerField()
	nr_ustawy=models.IntegerField()
	tytul=models.TextField()
	link=models.TextField()
	nr_importu=models.IntegerField()

	class Meta:
		db_table="ustawy"
 
class Dane_osoba(models.Model):
	id_osoby=models.IntegerField(primary_key=True)
	imie=models.CharField(max_length=30)
	nazwisko=models.CharField(max_length=50)
	haslo=models.CharField(max_length=50)
	data=models.DateField()
	email=models.CharField(max_length=70)
	nr_telefonu=models.IntegerField()
	plec=models.BooleanField(null=True)
	PESEL=models.TextField()
	class Meta:
		db_table="dane_osoba"
