from __future__ import unicode_literals
from django.contrib.auth.models import User
from transaksi_ahs.models import AHS
from django.db import models

# Create your models here.
class RAP(models.Model):
	nomor_ahs = models.ForeignKey(AHS)
	volume_rab =  models.IntegerField(blank=False)
	harga_satuan_rab = models.FloatField(blank=False)
	volume_rap =  models.IntegerField(blank=False)
	catatan =  models.TextField(max_length=200, blank=True) 
	updated_date = models.DateTimeField(auto_now=True)
	created_date =  models.DateTimeField(auto_now_add=True)
	updated_by = models.ForeignKey(User, related_name='rap_updated_by')
	created_by = models.ForeignKey(User, related_name='rap_created_by')
	

	class Meta:
		verbose_name = "rap"	    
		verbose_name_plural = "rap"	
