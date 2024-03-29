# Generated by Django 3.2.7 on 2022-09-24 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('type', models.CharField(choices=[('PROVA', 'PROVA'), ('ATIVIDADE', 'ATIVIDADE')], max_length=255, verbose_name='tipo')),
                ('date_init', models.DateTimeField(blank=True, null=True, verbose_name='data início')),
                ('date_end', models.DateTimeField(blank=True, null=True, verbose_name='data fim')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('class_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.classsubject', verbose_name='matéria turma')),
                ('class_subject_history', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.classsubjecthistory', verbose_name='aula')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolWorkManage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.BooleanField(default=False, verbose_name='entregue')),
                ('grade', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='nota')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('school_work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_work.schoolwork', verbose_name='atividade')),
                ('student_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.studentsubject', verbose_name='matéria aluno')),
            ],
        ),
    ]
