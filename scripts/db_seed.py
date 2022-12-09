from faker import Faker
from school_class.models import SchoolClass
from teacher.models import Teacher
from student.models import Student
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
import django
import os
import sys

from django.db import IntegrityError


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'agenda_professor_api.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      "agenda_professor_api.settings")
django.setup()


fake = Faker('pt_BR')

series = [6, 7, 8, 9]
ids = ["A", "B"]
turnos = ["MANHÃ", "TARDE"]


def generate_school_classes_subjects(instance):
    materias = ["Português", "Matemática", "História", "Geografia", "Ciências", "Literatura", "Inglês", "Religião", "Educação física"]

    for materia in materias:
        teacher = Teacher.objects.filter(formacao=materia)
        if teacher.exists():
            instance.classsubject_set.create(
                subject=materia,
                school_class=instance,
                teacher=teacher.first()
            )


def generate_school_classes():
    for serie in series:
        for id in ids:
            for turno in turnos:
                instance, created = SchoolClass.objects.get_or_create(
                    serie=serie,
                    identification=id,
                    shift=turno
                )

                if created:
                    generate_school_classes_subjects(instance)


def generate_teachers():
    materias = ["Português", "Matemática", "História", "Geografia", "Ciências", "Literatura", "Inglês", "Religião", "Educação física"]

    for materia in materias:
        teacher, _ = Teacher.objects.get_or_create(
            cpf=fake.cpf(),
            birth_date=fake.date_of_birth(),
            formacao=materia,
            address_street=fake.address(),
            address_number=fake.building_number(),
            address_district=fake.bairro()
        )
        user = generate_user("2" + teacher.registration_id)
        teacher.user = user
        teacher.save()


def generate_user(registration_id):
    try:
        user, created = User.objects.get_or_create(
            username=registration_id,
            email=fake.email,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            password=make_password('1234')
        )
    except IntegrityError as e:
        print(e)
        generate_user(registration_id)
    except Exception as e:
        print(type(e).__name__)

    return user


def generate_students():
    for index in range(40):
        target_serie = series[0]
        target_id = ids[0]
        target_shift = turnos[0]

        if index >= 10:
            target_serie = series[1]
        if index >= 20:
            target_serie = series[2]
            target_id = ids[1]
        if index >= 30:
            target_serie = series[3]

        if index >= 20:
            target_shift = turnos[1]

        student, _ = Student.objects.get_or_create(
            responsible_name=fake.name(),
            responsible_contact=fake.phone_number(),
            cpf=fake.cpf(),
            birth_date=fake.date_of_birth(),
            address_street=fake.address(),
            address_number=fake.building_number(),
            address_district=fake.bairro(),
            serie=target_serie,
            identification=target_id,
            shift=target_shift
        )
        user = generate_user("1" + student.registration_id)

        student.user = user
        student.save()


def db_seed():
    generate_teachers()
    generate_students()
    generate_school_classes()


if __name__ == "__main__":
    print("Iniciado o script...")
    db_seed()
    print("Pronto! :)")
