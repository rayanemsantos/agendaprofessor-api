from django.utils import timezone
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from localflavor.br.models import BRCPFField

UserModel = get_user_model()

class BaseUser(models.Model):
    '''
    Classe abstrata para dados de usuário
    '''
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    cpf = BRCPFField(_("CPF"), unique=True, db_index=True)
    birth_date = models.DateField(_("data de nascimento"), blank=True, null=True)
    avatar = models.ImageField(_("avatar"), upload_to='avatar/', blank=True, null=True)
    creation_datetime = models.DateTimeField(editable=False)
    edition_datetime = models.DateTimeField(_("última atualização"), null=True, blank=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return str(self.user.get_full_name())
    
    def save(self, *args, **kwargs):
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(BaseUser, self).save(*args, **kwargs)

    @property
    def full_name(self):
        return self.user.get_full_name()

    @property
    def email(self):
        return self.user.email

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name        