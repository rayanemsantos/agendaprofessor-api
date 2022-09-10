from django.test import TestCase

from student.models import Student

class StudentTestCase(TestCase):
  
    def setUp(self):
        Student.objects.create(
            full_name='Rayane Mariaa dos Santos',
            responsible_contact='Juvenal dos Santos',
            address_street='Rua A',
            address_number='1045',
            address_district='Distrito 12'
        )

    def test_get(self):
        student = Student.objects.first()
        self.assertIsInstance(student, Student)

    def test_update(self):
        student = Student.objects.first()
        student.full_name ='Rayane Maria dos Santos'
        student.save()
        self.assertEqual(student.full_name, 'Rayane Maria dos Santos')
        

    def test_delete(self):
        student = Student.objects.first()
        student.delete()
        self.assertFalse(student.id)
        self.assertIsInstance(student, Student)

