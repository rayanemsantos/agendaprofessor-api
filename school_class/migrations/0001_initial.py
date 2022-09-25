# Generated by Django 3.2.7 on 2022-09-24 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('Matemática', 'Matemática'), ('Inglês', 'Inglês'), ('Química', 'Química'), ('Espanhol', 'Espanhol'), ('Biologia', 'Biologia'), ('Gramática', 'Gramática'), ('Filosofia', 'Filosofia'), ('Física', 'Física'), ('História', 'História'), ('Português', 'Português'), ('Literatura', 'Literatura'), ('Geografia', 'Geografia'), ('Ciências', 'Ciências'), ('Artes', 'Artes'), ('Educação física', 'Educação física'), ('Redação', 'Redação')], max_length=255, verbose_name='materia')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
            ],
        ),
        migrations.CreateModel(
            name='ClassSubjectHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=255, null=True, verbose_name='conteúdo')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comentário')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('class_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.classsubject', verbose_name='matéria da turma')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('class_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.classsubject', verbose_name='matéria turma')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='aluno')),
            ],
        ),
        migrations.CreateModel(
            name='StudentSubjectAverageGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_grade', models.DecimalField(decimal_places=1, max_digits=10, verbose_name='nota média')),
                ('period', models.CharField(choices=[('Bimestral', 'Bimestral'), ('Trimestral', 'Trimestral'), ('Semestral', 'Semestral'), ('Anual', 'Anual')], max_length=255, verbose_name='período')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('student_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.studentsubject', verbose_name='matéria aluno')),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(blank=True, max_length=255, null=True, verbose_name='série')),
                ('identification', models.CharField(blank=True, max_length=255, null=True, verbose_name='identificação')),
                ('shift', models.CharField(choices=[('MANHÃ', 'MANHÃ'), ('TARDE', 'TARDE'), ('NOITE', 'NOITE')], max_length=255, verbose_name='turno')),
                ('ano', models.PositiveIntegerField(blank=True, null=True, verbose_name='ano')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
            ],
            options={
                'unique_together': {('serie', 'identification', 'shift')},
            },
        ),
        migrations.CreateModel(
            name='ClassSubjectSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_week', models.CharField(choices=[('Segunda-feira', 'Segunda-feira'), ('Terça-feira', 'Terça-feira'), ('Quarta-feira', 'Quarta-feira'), ('Quinta-feira', 'Quinta-feira'), ('Sexta-feira', 'Sexta-feira'), ('Sábado-feira', 'Sábado-feira'), ('Domingo-feira', 'Domingo-feira')], max_length=255, verbose_name='dia da semana')),
                ('hour_init', models.TimeField(blank=True, null=True, verbose_name='hora início')),
                ('hour_end', models.TimeField(blank=True, null=True, verbose_name='hora fim')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('class_subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.classsubject', verbose_name='matéria da turma')),
            ],
        ),
        migrations.CreateModel(
            name='ClassSubjectHistoryPresence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.BooleanField(verbose_name='presente')),
                ('creation_datetime', models.DateTimeField(editable=False)),
                ('edition_datetime', models.DateTimeField(blank=True, null=True, verbose_name='última atualização')),
                ('class_subject_history', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.classsubjecthistory', verbose_name='aula')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student', verbose_name='aluno')),
            ],
        ),
        migrations.AddField(
            model_name='classsubject',
            name='school_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='school_class.schoolclass', verbose_name='turma'),
        ),
        migrations.AddField(
            model_name='classsubject',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher', verbose_name='professor'),
        ),
    ]
