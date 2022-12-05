from django.contrib import admin
from .models import Images, Categories, Locations

# Register your models here.

class ImagesAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Images, ImagesAdmin)
admin.site.register(Categories)
admin.site.register(Locations)