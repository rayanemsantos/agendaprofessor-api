import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete, pre_save

from teacher.models import Teacher
from student.models import Student

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
    ("Religião", "Religião"),
]

GRADE_PERIOD_CHOICES = [
    ("1 Bimestre", "1 Bimestre"),
    ("2 Bimestre", "2 Bimestre"),
    ("3 Bimestre", "3 Bimestre"),
    ("4 Bimestre", "4 Bimestre"),
]

WEEKS_CHOICES = [
    ("Segunda-feira", "Segunda-feira"),
    ("Terça-feira", "Terça-feira"),
    ("Quarta-feira", "Quarta-feira"),
    ("Quinta-feira", "Quinta-feira"),
    ("Sexta-feira", "Sexta-feira"),
    ("Sábado-feira", "Sábado-feira"),
    ("Domingo-feira", "Domingo-feira"),
]


class SchoolClass(models.Model):
    '''
    Classe que representa uma turma
    '''
    serie = models.CharField(_("série"), max_length=255, null=True, blank=True)
    identification = models.CharField(
        _("identificação"), max_length=255, null=True, blank=True)
    shift = models.CharField(_("turno"), max_length=255, choices=SHIFT_CHOICES)
    ano = models.PositiveIntegerField(_("ano"), null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    class Meta:
        unique_together = ('serie', 'identification', 'shift', )

    def __str__(self):
        return "{} ano {} | {}".format(self.serie, self.identification, self.shift)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
            self.ano = datetime.datetime.now().year
        self.edition_datetime = timezone.now()
        return super(SchoolClass, self).save(*args, **kwargs)

    @property
    def label(self):
        return self.serie + " " + self.identification + " | " + self.shift


# @receiver(post_save, sender=SchoolClass)
# def on_post_save_schoolclass(sender, instance=None, **kwargs):
#     materias = ["Português", "Matemática", "História", "Geografia", "Ciências", "Literatura", "Inglês", "Religião", "Educação física"]

#     if not instance.classsubject_set.exists():
#         for materia in materias:
#             teacher = Teacher.objects.filter(formacao=materia)
#             if teacher.exists():
#                 instance.classsubject_set.create(
#                     subject=materia,
#                     school_class=instance,
#                     teacher=teacher.first()
#                 )


class ClassSubject(models.Model):
    '''
    Classe que representa uma matéria de uma turma
    '''
    school_class = models.ForeignKey(SchoolClass, verbose_name=_("turma"),
                                     on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, verbose_name=_("professor"),
                                on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(
        _("materia"), max_length=255, choices=SUBJECT_CHOICES)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.school_class.__str__() + " " + self.subject + " " + self.teacher.__str__()

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(ClassSubject, self).save(*args, **kwargs)

    @property
    def label(self):
        return self.subject + " " + self.school_class.label


@receiver(post_save, sender=ClassSubject)
def on_post_save_classsubject(sender, instance=None, **kwargs):
    for item in Student.objects.filter(
        serie=instance.school_class.serie,
        identification=instance.school_class.identification,
        shift=instance.school_class.shift,
    ):
        instance.studentsubject_set.get_or_create(
            class_subject=instance,
            student=item,
        )


class ClassSubjectSchedule(models.Model):
    '''
    Classe que representa a frequência de aula de uma máteria
    '''
    class_subject = models.ForeignKey(ClassSubject, verbose_name=_("matéria da turma"),
                                      on_delete=models.CASCADE, null=True, blank=True)
    day_week = models.CharField(
        _("dia da semana"), max_length=255, choices=WEEKS_CHOICES)
    hour_init = models.TimeField(_("hora início"), null=True, blank=True)
    hour_end = models.TimeField(_("hora fim"), null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(ClassSubjectSchedule, self).save(*args, **kwargs)


class ClassSubjectHistory(models.Model):
    '''
    Classe que representa o registro de aula de uma matéria
    '''
    content = models.CharField(
        _("conteúdo"), max_length=255, null=True, blank=True)
    comment = models.TextField(_("comentário"), null=True, blank=True)
    class_subject = models.ForeignKey(ClassSubject, verbose_name=_("matéria da turma"),
                                      on_delete=models.CASCADE, null=True, blank=True)
    register_datetime = models.DateTimeField(_("Data de registro"), null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    def __str__(self):
        return "{} dia {}".format(self.class_subject, self.creation_datetime.strftime("%d/%m"))

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(ClassSubjectHistory, self).save(*args, **kwargs)


class ClassSubjectHistoryPresence(models.Model):
    '''
    Classe que representa o controle de presença de uma aula
    '''
    class_subject_history = models.ForeignKey(ClassSubjectHistory, verbose_name=_("aula"),
                                              on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, verbose_name=_("aluno"),
                                on_delete=models.CASCADE, null=True, blank=True)
    presence = models.BooleanField(_("presente"))
    register_datetime = models.DateTimeField(_("Data de registro"), null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(ClassSubjectHistoryPresence, self).save(*args, **kwargs)


class StudentSubject(models.Model):
    '''
    Classe que representa uma matéria de um aluno
    '''
    class_subject = models.ForeignKey(ClassSubject, verbose_name=_("matéria turma"),
                                      on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, verbose_name=_("aluno"),
                                on_delete=models.CASCADE, null=True, blank=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    def __str__(self):
        return self.class_subject.school_class.__str__() + " " + self.class_subject.subject

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(StudentSubject, self).save(*args, **kwargs)


class StudentSubjectAverageGrade(models.Model):
    '''
    Classe que representa as médias de uma determinada matéria de um aluno
    '''
    student_subject = models.ForeignKey(StudentSubject, verbose_name=_("matéria aluno"),
                                        on_delete=models.CASCADE, null=True, blank=True)
    average_grade = models.DecimalField(
        _("nota média"), max_digits=10, decimal_places=1)
    period = models.CharField(
        _("período"), max_length=255, choices=GRADE_PERIOD_CHOICES)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(StudentSubjectAverageGrade, self).save(*args, **kwargs)
