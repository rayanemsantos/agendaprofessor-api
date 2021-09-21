from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

class Student(models.Model):

    registration_id = models.PositiveIntegerField(_("matrícula"), null=True, blank=True) 
    responsible_name = models.CharField(_("nome do responsável"), max_length=255, null=True, blank=True) 
    responsible_contact = models.CharField(_("contato do responsável"), max_length=255, null=True, blank=True) 
    address_street = models.CharField(_("rua"), max_length=255, null=True, blank=True) 
    address_number = models.CharField(_("número"), max_length=255, null=True, blank=True) 
    address_district = models.CharField(_("bairro"), max_length=255, null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(Student, self).save(*args, **kwargs)