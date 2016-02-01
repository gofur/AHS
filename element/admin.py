from django.contrib import admin

# Register your models here.
from .models import Element, JenisElement

class ElementModelAdmin(admin.ModelAdmin):
	list_display = ['jenis_element','kode_element','nama_element', 'updated', 'timestamp']
	list_filter = ['kode_element', 'nama_element']
	search_fields = ['kode_element', 'nama_element'] 
	class Meta:
		model = Element


class JenisElementModelAdmin(admin.ModelAdmin):
	list_display = ['kode_jenis_element','nama_jenis_element']
	list_filter = ['kode_jenis_element', 'nama_jenis_element']
	search_fields = ['kode_jenis_element', 'nama_jenis_element'] 
	class Meta:
		model = JenisElement



admin.site.register(Element, ElementModelAdmin)
admin.site.register(JenisElement, JenisElementModelAdmin)