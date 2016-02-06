from __future__ import unicode_literals
from django.db import models

# Create your models here.
class JenisElement(models.Model):
	kode_jenis_element = models.CharField(max_length=8, unique=True)
	nama_jenis_element = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nama_jenis_element

	def __str__(self):
		return self.nama_jenis_element


class Element(models.Model):
	jenis_element = models.ForeignKey(JenisElement)
	kode_element = models.CharField(max_length=8, unique=True)
	nama_element = models.CharField(max_length=100)
	uraian_element = models.CharField(max_length=100, blank=True)
	keterangan = models.TextField(max_length=200, blank=True)
	satuan_element = models.CharField(max_length=30, blank=True)
	harga_satuan = models.FloatField(blank=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp =  models.DateTimeField(auto_now=False, auto_now_add=True)


	def __unicode__(self):
		return self.kode_element

	def __str__(self):
		return self.kode_element


