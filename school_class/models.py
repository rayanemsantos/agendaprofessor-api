from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone

from teacher.models import Teacher
from student.models import Student
from school_work.models import SchoolWork

SHIFT_CHOICES = [
    ("MANHÃ", "MANHÃ"),
    ("TARDE", "TARDE"),
    ("NOITE", "NOITE"),
]

SUBJECT_CHOICES = [
    ("Matemática", "Matemática"),
    ("Inglês", "Inglês"),
    ("Química", "Química"),
    ("Espanhol", "Espanhol"),
    ("Biologia", "Biologia"),
    ("Gramática", "Gramática"),
    ("Filosofia", "Filosofia"),
    ("Física", "Física"),
    ("História", "História"),
    ("Português", "Português"),       
    ("Literatura", "Literatura"),
    ("Geografia", "Geografia"),
    ("Ciências", "Ciências"),
    ("Artes", "Artes"),
    ("Educação física", "Educação física"),
    ("Redação", "Redação"),
]

class SchoolClass(models.Model):

    serie = models.CharField(_("matrícula"), max_length=255, null=True, blank=True) 
    shift = models.CharField(_("turno"), max_length=255, choices=SHIFT_CHOICES)    
    ano = models.PositiveIntegerField(_("ano"), null=True, blank=True )    
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.serie + " " + self.shift

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolClass, self).save(*args, **kwargs)


class SchoolClassSubject(models.Model):

    school_class = models.ForeignKey(SchoolClass, verbose_name=_("turma"),
                                     on_delete=models.CASCADE, null=True, blank=True)        
    teacher = models.ForeignKey(Teacher, verbose_name=_("professor"),
                                 on_delete=models.CASCADE, null=True, blank=True)    
    subject = models.CharField(_("materia"), max_length=255, choices=SUBJECT_CHOICES)                                            
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolClassSubject, self).save(*args, **kwargs)

class SchoolClassStudent(models.Model):

    school_class_subject = models.ForeignKey(SchoolClassSubject, verbose_name=_("turma"),
                                     on_delete=models.CASCADE, null=True, blank=True)        
    student = models.ForeignKey(Student, verbose_name=_("aluno"),
                                 on_delete=models.CASCADE, null=True, blank=True)                                              
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolClassStudent, self).save(*args, **kwargs)


class SchoolClassSubjectHistory(models.Model):

    content = models.CharField(_("conteúdo"), max_length=255, null=True, blank=True) 
    comment = models.TextField(_("comentário") ,null=True, blank=True) 
    school_class_subject = models.ForeignKey(SchoolClassSubject, verbose_name=_("turma"),
                                             on_delete=models.CASCADE, null=True, blank=True)        
    homework = models.ForeignKey(SchoolWork, related_name='homework', verbose_name=_("trabalho de casa"),
                                 on_delete=models.CASCADE, null=True, blank=True)    
    classwork = models.ForeignKey(SchoolWork, related_name='classwork', verbose_name=_("trabalho de classe"),
                                 on_delete=models.CASCADE, null=True, blank=True)                                                                               
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(SchoolClassSubjectHistory, self).save(*args, **kwargs)


class AttendanceManage(models.Model):

    school_class_subject = models.ForeignKey(SchoolClassSubject, verbose_name=_("turma"),
                                             on_delete=models.CASCADE, null=True, blank=True)    
    student = models.ForeignKey(Student, verbose_name=_("aluno"),
                                on_delete=models.CASCADE, null=True, blank=True)     
    presence = models.BooleanField(_("presente"))                                                                    
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(AttendanceManage, self).save(*args, **kwargs)