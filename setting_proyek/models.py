from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proyek(models.Model):
	nomor_proyek =	models.IntegerField()
	nama_proyek = models.CharField(max_length=200, blank=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp =  models.DateTimeField(auto_now=False, auto_now_add=True)
	pengguna = models.CharField(max_length=4, choices= ((u'H', u'High',), (u'M', u'Medium'), (u'L', u'Low')))

	def __unicode__(self):
		return self.nomor_proyek

	def __str__(self):
		return self.nomor_proyek