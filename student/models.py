import datetime
import random
from django.db import models
from django.utils.translation import gettext as _
from base_auth.models import BaseUser

SHIFT_CHOICES = [
    ("MANHÃ", "MANHÃ"),
    ("TARDE", "TARDE"),
    ("NOITE", "NOITE"),
]


class Student(BaseUser):
    '''
    Classe que representa um estudante
    '''
    registration_id = models.CharField(_("código de matrícula"), max_length=7, editable=False)

    responsible_name = models.CharField(_("nome do responsável"), max_length=255, null=True, blank=True) 
    responsible_contact = models.CharField(_("contato do responsável"), max_length=255, null=True, blank=True) 

    address_street = models.CharField(_("rua"), max_length=255, null=True, blank=True)
    address_number = models.CharField(_("número"), max_length=255, null=True, blank=True)
    address_district = models.CharField(_("bairro"), max_length=255, null=True, blank=True) 

    serie = models.CharField(_("série"), max_length=255, null=True, blank=True)
    identification = models.CharField(
        _("identificação"), max_length=255, null=True, blank=True)
    shift = models.CharField(_("turno"), max_length=255, choices=SHIFT_CHOICES, null=True, blank=True)

    def __str__(self):
        return '' if not self.full_name else self.full_name

    def save(self, *args, **kwargs):
        if not self.registration_id:
            code = self.set_registration_id()       
            self.registration_id = code 
        return super(Student, self).save(*args, **kwargs)

    def set_registration_id(self):
        while 1:
            now = datetime.datetime.now()
            code = str(random.randrange(100, 999)) + str(now.year)[:4]
            try:
                Student.objects.get(registration_id=code)
            except:
                return code
