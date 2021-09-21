from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from localflavor.br.models import BRCPFField

UserModel = get_user_model()

class AuthUser(models.Model):
    '''
    Atributos herdados: name ...
    '''
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    cpf = BRCPFField(_("CPF"), unique=True, db_index=True)
    birth_date = models.DateField(_("data de nascimento"), blank=True, null=True)
    avatar = models.ImageField(_("avatar"), upload_to='avatar/', blank=True, null=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return str(self.user.get_full_name())
    
    @property
    def name(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)