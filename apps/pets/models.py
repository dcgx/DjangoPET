from django.db import models
from django.urls import reverse_lazy

class BaseName(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AnimalType(BaseName):
    minimum_age = models.IntegerField(verbose_name='Edad Mínima (meses)')

    class Meta:
        verbose_name = 'Tipo de Animal'
        verbose_name_plural = 'Tipos de Animales'


class Pet(BaseName):
    image = models.ImageField(upload_to='pets', verbose_name='Foto de la Mascota')
    birth_date = models.DateField(verbose_name='Fecha de Nacimiento')
    medical_history = models.TextField(verbose_name='Historial Médico', blank=True)
    owner_name = models.CharField(max_length=150, verbose_name='Nombre del Dueño')
    owner_contact = models.CharField(max_length=100, verbose_name='Contacto del Dueño')
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE, verbose_name='Tipo de Animal')

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'

    def get_edit_url(self):
        return reverse_lazy('pets:pet-edit', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse_lazy('pets:pet-delete', kwargs={'pk': self.pk})

    def get_detail_url(self):
        return reverse_lazy('pets:pet-detail', kwargs={'pk': self.pk})
