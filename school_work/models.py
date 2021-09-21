from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from student.models import Student

class SchoolWork(models.Model):

    title = models.CharField(_("título"), max_length=255, null=True, blank=True) 
    description = models.TextField(_("descrição"), null=True, blank=True) 
    date_init = models.DateTimeField(_("data início"), null=True, blank=True)
    date_end = models.DateTimeField(_("data fim"), null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolWork, self).save(*args, **kwargs)

class SchoolWorkDeliveryManage(models.Model):

    school_work = models.ForeignKey(SchoolWork, verbose_name=_("atividade"),
                                    on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, verbose_name=_("aluno"),
                                on_delete=models.CASCADE, null=True, blank=True)     
    delivered = models.BooleanField(_("entregue"))                                                                    
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.school_work +  " " + self.student

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolWorkDeliveryManage, self).save(*args, **kwargs)