from django.contrib import admin
# Register your models here.
from .models import AHS
from setting_proyek.models import Proyek
class AHSModelAdmin(admin.ModelAdmin):
	# list_display = ['nomor_ahs', 'nomor_proyek', 'nama_ahs', 'kode_element', 'harga_satuan', 'koefisien', 'catatan', 'updated_date', 'updated_by']
	list_display = ['nomor_ahs', 'get_name','nama_ahs', 'harga_satuan']
	list_filter = ['nomor_ahs', 'nama_ahs']
	# search_fields = ['nomor_proyek', 'nama_proyek']
	class Meta:
		model = AHS

	def get_name(self, obj):
		return obj.nomor_proyek.nomor_proyek
	get_name.admin_order_field  = 'nomor_proyek'  #Allows column order sorting
	get_name.short_description = 'Nomor Proyek'  #Renames column head

admin.site.register(AHS, AHSModelAdmin)