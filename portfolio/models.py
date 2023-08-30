from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    link = models.URLField(verbose_name="Enlace",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizacion")
    
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        #ordenar por creacion nuevo a mas antiguo
        ordering = ["-created"]
        
    #que muestre el nombre del proyecto
    def __str__(self):
        return self.title
    