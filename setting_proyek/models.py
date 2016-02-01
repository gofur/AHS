from __future__ import unicode_literals
# from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Proyek(models.Model):
	nomor_proyek =	models.CharField(max_length=10,unique=True)
	nama_proyek = models.CharField(max_length=200, blank=False)
	updated = models.DateTimeField(auto_now=True)
	timestamp =  models.DateTimeField(auto_now_add=True)
	pengguna = models.ForeignKey(User)


	def __unicode__(self):
		return self.nomor_proyek

	def __str__(self):
		return self.nomor_proyek

	# def get_absolute_url(self):
 #   		return reverse("index", kwargs={"id": id})