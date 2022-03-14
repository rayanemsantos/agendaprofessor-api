from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

class CalendarEvent(models.Model):

    title = models.CharField(_("título"), max_length=255, null=True, blank=True) 
    description = models.TextField(_("descrição"), null=True, blank=True) 
    date_schedule = models.DateTimeField(_("data agendada"), null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(CalendarEvent, self).save(*args, **kwargs)


class Address(models.Model):
    ''' Classe que representa a endereço '''

    address = models.CharField(_("endereço"), max_length=255, null=True, blank=True)
    number = models.CharField(_("número"), max_length=10, blank=True, null=True)
    district = models.CharField(_("bairro"), max_length=255, null=True, blank=True)
    complement = models.CharField(_("complemento"), max_length=100, blank=True, null=True)
    zip_code = models.CharField(_("cep"), max_length=10, null=True, blank=True)
    creation_datetime = models.DateTimeField(_("data de criação"), editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    class Meta:
        ordering = ('address',)
        verbose_name = _('endereço')
        verbose_name_plural = _('endereços')

    def save(self, *args, **kwargs):
        # Atualizar datas criacao edicao
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        super(Address, self).save(*args, **kwargs)