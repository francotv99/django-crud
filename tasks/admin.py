from django.contrib import admin
from .models import Pais, Estado
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
   readonly_fields=("created",)

##Vincular la tabla con el programa en este 

admin.site.register(Pais)
admin.site.register(Estado)