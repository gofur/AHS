from django.contrib import admin

# Register your models here.
from .models import AHS

class AHSModelAdmin(admin.ModelAdmin):
	list_display = ['nomor_ahs','nomor_proyek', 'nama_ahs', 'kode_element', 'harga_satuan', 'koefisien','catatan','updated_date','updated_by']
	# list_filter = ['nomor_proyek', 'nama_proyek']
	# search_fields = ['nomor_proyek', 'nama_proyek'] 
	class Meta:
		model = AHS


admin.site.register(AHS, AHSModelAdmin)