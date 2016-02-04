from __future__ import unicode_literals
from django.contrib.auth.models import User
from element.models import Element
from setting_proyek.models import Proyek
from django.db import models


# Create your models here.
class AHS(models.Model):
	nomor_ahs = models.CharField(max_length=7)
	nomor_proyek =	models.ForeignKey(Proyek)
	nama_ahs = models.CharField(max_length=120, blank=False)
	kode_element = models.ForeignKey(Element)
	harga_satuan = models.FloatField(blank=False)
	koefisien = models.FloatField(blank=False)
	catatan =  models.TextField(max_length=200, blank=True) 
	updated_date = models.DateTimeField(auto_now=True)
	created_date =  models.DateTimeField(auto_now_add=True)
	updated_by = models.ForeignKey(User, related_name='ahs_updated_by')
	created_by = models.ForeignKey(User, related_name='ahs_created_by')

	def __unicode__(self):
		return self.nomor_ahs

	def __str__(self):
		return self.nomor_ahs
		
	class Meta:
		verbose_name = "ahs"	    
		verbose_name_plural = "ahs"	

