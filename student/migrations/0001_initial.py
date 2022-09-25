# Generated by Django 3.2.7 on 2022-09-24 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', localflavor.br.models.BRCPFField(db_index=True, max_length=14, unique=True, verbose_name='CPF')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='data de nascimento')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/', verbose_name='avatar')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('registration_id', models.CharField(editable=False, max_length=7, verbose_name='código de matrícula')),
                ('responsible_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='nome do responsável')),
                ('responsible_contact', models.CharField(blank=True, max_length=255, null=True, verbose_name='contato do responsável')),
                ('address_street', models.CharField(blank=True, max_length=255, null=True, verbose_name='rua')),
                ('address_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='número')),
                ('address_district', models.CharField(blank=True, max_length=255, null=True, verbose_name='bairro')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
