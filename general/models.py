from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

class CalendarEvent(models.Model):

    color = models.CharField(_("cor"), max_length=255, null=True, blank=True) 
    title = models.CharField(_("título"), max_length=255, null=True, blank=True) 
    description = models.TextField(_("descrição"), null=True, blank=True) 
    
    date_schedule = models.DateTimeField(_("data agendada"), null=True, blank=True)
    date_init_schedule = models.DateTimeField(_("data início agendada"), null=True, blank=True)
    date_end_schedule = models.DateTimeField(_("data início agendada"), null=True, blank=True)
    
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(CalendarEvent, self).save(*args, **kwargs)