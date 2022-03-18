from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from base_auth.models import AuthUser

JOB_TITLE_CHOICES = [
    ("DIRETOR", "DIRETOR"),
    ("COORDENADOR", "COORDENADOR"),
    ("SECRETÁRIO", "SECRETÁRIO"),
]

class SchoolStaff(AuthUser):

    job_title = models.CharField(_("cargo"), max_length=255, choices=JOB_TITLE_CHOICES)  
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.user.username + ' - ' + self.job_title

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolStaff, self).save(*args, **kwargs)