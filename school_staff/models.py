from django.db import models
from django.utils.translation import gettext as _

from base_auth.models import BaseUser

JOB_TITLE_CHOICES = [
    ("DIRETOR", "DIRETOR"),
    ("COORDENADOR", "COORDENADOR"),
    ("SECRETÁRIO", "SECRETÁRIO"),
]

class SchoolStaff(BaseUser):
    '''
        Classe que representa a staff da escola
    '''
    job_title = models.CharField(_("cargo"), max_length=255, choices=JOB_TITLE_CHOICES)  

    def __str__(self):
        return self.full_name + ' - ' + self.job_title