# Generated by Django 3.2.7 on 2022-12-08 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_class', '0002_alter_classsubject_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsubjectaveragegrade',
            name='period',
            field=models.CharField(choices=[('1 Bimestre', '1 Bimestre'), ('2 Bimestre', '2 Bimestre'), ('3 Bimestre', '3 Bimestre'), ('4 Bimestre', '4 Bimestre')], max_length=255, verbose_name='período'),
        ),
    ]
