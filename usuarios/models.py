from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Número de Teléfono")
    address = models.TextField(blank=True, null=True, verbose_name="Dirección")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    profile_image = models.ImageField(upload_to="profile_images/", blank=True, null=True, verbose_name="Imagen de Perfil")

    # Verificacion de email
    #is_email_verified = models.BooleanField(default=False, verbose_name="Email Verificado")

    def __str__(self):
        return "Hola, mi nombre es {}".format(self.username)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
