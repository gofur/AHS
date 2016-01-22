from django.contrib import admin

# Register your models here.
from .models import Element

class ElementModelAdmin(admin.ModelAdmin):
	list_display = ['kode_element','nama_element', 'updated', 'timestamp']
	list_filter = ['kode_element', 'nama_element']
	search_fields = ['kode_element', 'nama_element'] 
	class Meta:
		model = Element



admin.site.register(Element, ElementModelAdmin)