import datetime
import random
from django.db import models
from django.utils.translation import gettext as _
from base_auth.models import BaseUser


class Teacher(BaseUser):
    '''
    Classe que representa um professor
    '''
    registration_id = models.CharField(_("código de matrícula"), max_length=7, editable=False)
    
    formacao = models.CharField(_("formação"), max_length=255, null=True, blank=True) 

    address_street = models.CharField(_("rua"), max_length=255, null=True, blank=True)
    address_number = models.CharField(_("número"), max_length=255, null=True, blank=True)
    address_district = models.CharField(_("bairro"), max_length=255, null=True, blank=True) 

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.registration_id:
            code = self.set_registration_id()
            self.registration_id = code
        return super(Teacher, self).save(*args, **kwargs)

    def set_registration_id(self):
        while 1:
            now = datetime.datetime.now()
            code = str(random.randrange(100, 999)) + str(now.year)[:4]
            try:
                Teacher.objects.get(registration_id=code)
            except:
                return code