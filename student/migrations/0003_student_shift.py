# Generated by Django 3.2.7 on 2022-12-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='shift',
            field=models.CharField(blank=True, choices=[('MANHÃ', 'MANHÃ'), ('TARDE', 'TARDE'), ('NOITE', 'NOITE')], max_length=255, null=True, verbose_name='turno'),
        ),
    ]
