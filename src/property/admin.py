from django.contrib import admin

# Register your models here.
from .models import Property , Category , Reserve




class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'type' , 'category' , 'area' , 'rooms_number' , 'beds_number']
    search_fields = ['name' , 'type' , 'category']
    list_filter = ['category', 'type']

admin.site.register(Property , PropertyAdmin)
admin.site.register(Category)
admin.site.register(Reserve)