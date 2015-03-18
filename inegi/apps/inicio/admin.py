from django.contrib import admin
from . models import SistemaOperativo, Equipo, Parche, File, Update
# Register your models here.
admin.site.register(SistemaOperativo)
admin.site.register(Equipo)
admin.site.register(Parche)
admin.site.register(File)
admin.site.register(Update)