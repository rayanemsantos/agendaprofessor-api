from django.test import TestCase

from teacher.models import Teacher

class TeacherTestCase(TestCase):
  
    def setUp(self):
        Teacher.objects.create(
            full_name='Rayane Mariaa dos Santos',
            formacao='Licenciatura Português',
            address_street='Rua A',
            address_number='1045',
            address_district='Distrito 14'
        )

    def test_get(self):
        teacher = Teacher.objects.first()
        self.assertIsInstance(teacher, Teacher)

    def test_update(self):
        teacher = Teacher.objects.first()
        teacher.full_name ='Rayane Maria dos Santos'
        teacher.save()
        self.assertEqual(teacher.full_name, 'Rayane Maria dos Santos')
        

    def test_delete(self):
        teacher = Teacher.objects.first()
        teacher.delete()
        self.assertFalse(teacher.id)
        self.assertIsInstance(teacher, Teacher)

