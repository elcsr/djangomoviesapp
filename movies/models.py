from django.db import models
from django.utils import timezone
class Post(models.Model):
    usuario = models.ForeignKey('auth.User')
    pelicula= models.CharField(max_length=200)
    Director = models.CharField(max_length=200)
    FechaPublicacionPelicula= models.DateTimeField(blank=True, null=True)
    calificacion = models.CharField(max_length=200)
    CasaProductora= models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
def publish(self):
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
# Create your models here.
