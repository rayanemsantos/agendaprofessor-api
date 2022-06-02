import uuid
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

# from base_auth.models import AuthUser

class Teacher(models.Model):

    full_name = models.CharField(_("nome completo"), max_length=255, null=True, blank=True) 
    registration_id = models.UUIDField(_("matrícula"), default=uuid.uuid4, editable=False)
    formacao = models.CharField(_("formação"), max_length=255, null=True, blank=True) 

    address_street = models.CharField(_("rua"), max_length=255, null=True, blank=True)
    address_number = models.CharField(_("número"), max_length=255, null=True, blank=True)
    address_district = models.CharField(_("bairro"), max_length=255, null=True, blank=True) 

    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(Teacher, self).save(*args, **kwargs)