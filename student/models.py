import requests
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from general.models import Address

class Student(models.Model):

    full_name = models.CharField(_("nome completo"), max_length=255, null=True, blank=True) 
    registration_id = models.PositiveIntegerField(_("matrícula"), null=True, blank=True) 
    responsible_name = models.CharField(_("nome do responsável"), max_length=255, null=True, blank=True) 
    responsible_contact = models.CharField(_("contato do responsável"), max_length=255, null=True, blank=True) 
    address = models.ForeignKey(Address, verbose_name=_("endereço"),
                                on_delete=models.CASCADE, null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return '' if not self.full_name else self.full_name

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(Student, self).save(*args, **kwargs)