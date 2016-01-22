from django.contrib import admin

# Register your models here.
from .models import Proyek

class ProyekModelAdmin(admin.ModelAdmin):
	list_display = ['nomor_proyek','nama_proyek', 'updated', 'timestamp']
	list_filter = ['nomor_proyek', 'nama_proyek']
	search_fields = ['nomor_proyek', 'nama_proyek'] 
	class Meta:
		model = Proyek



admin.site.register(Proyek, ProyekModelAdmin)