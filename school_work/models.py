from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from school_class.models import ClassSubject, ClassSubjectHistory, StudentSubject

SCHOOL_WORK_CHOICES = [
    ("PROVA", "PROVA"),
    ("ATIVIDADE", "ATIVIDADE"),
]

class SchoolWork(models.Model):
    '''
    Classe que representa uma atividade de uma matéria
    '''
    class_subject = models.ForeignKey(ClassSubject, verbose_name=_("matéria turma"),
                                      on_delete=models.CASCADE, null=True, blank=True)       
    class_subject_history = models.ForeignKey(ClassSubjectHistory, verbose_name=_("aula"),
                                      on_delete=models.CASCADE, null=True, blank=True)                                             
    title = models.CharField(_("título"), max_length=255, null=True, blank=True) 
    description = models.TextField(_("descrição"), null=True, blank=True) 
    type = models.CharField(_("tipo"), max_length=255, choices=SCHOOL_WORK_CHOICES)                                                              
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


class SchoolWorkManage(models.Model):
    '''
    Classe que representa o controle de entrega e notas de uma atividade
    '''
    school_work = models.ForeignKey(SchoolWork, verbose_name=_("atividade"),
                                    on_delete=models.CASCADE, null=True, blank=True)                                                                     
    student_subject = models.ForeignKey(StudentSubject, verbose_name=_("matéria aluno"),
                                        on_delete=models.CASCADE, null=True, blank=True)     
    delivered = models.BooleanField(_("entregue"), default=False)
    grade = models.DecimalField(_("nota"), max_digits=10, decimal_places=1)      
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.school_work +  " " + self.student

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolWorkManage, self).save(*args, **kwargs)