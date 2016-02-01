from django.contrib import admin

# Register your models here.
from .models import RAP

class RAPModelAdmin(admin.ModelAdmin):
	list_display = ['nomor_ahs','volume_rab', 'harga_satuan_rab', 'volume_rap', 'catatan', 'updated_date','updated_by']
	# list_filter = ['nomor_proyek', 'nama_proyek']
	# search_fields = ['nomor_proyek', 'nama_proyek'] 
	class Meta:
		model = RAP


admin.site.register(RAP, RAPModelAdmin)
