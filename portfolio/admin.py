from django.contrib import admin
from .models import Project

# Register your models here
#mostrar la fecha de creacion y actualizacion de un projecto
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

#resgistrando en la pagina de administrador
admin.site.register(Project, ProjectAdmin)
