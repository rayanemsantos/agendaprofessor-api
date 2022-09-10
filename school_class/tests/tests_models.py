import datetime
from django.test import TestCase

from school_class.models import SchoolClass

class SchoolClassTestCase(TestCase):
  
    def setUp(self):
        SchoolClass.objects.create(
            serie='1',
            identification='B',
            shift='MANHÃ',
            ano=datetime.datetime.now().year,
        )

    def test_get(self):
        schoolclass = SchoolClass.objects.first()
        self.assertIsInstance(schoolclass, SchoolClass)

    def test_update(self):
        schoolclass = SchoolClass.objects.first()
        schoolclass.serie ='2'
        schoolclass.save()
        self.assertEqual(schoolclass.serie, '2')

    def test_delete(self):
        schoolclass = SchoolClass.objects.first()
        schoolclass.delete()
        self.assertFalse(schoolclass.id)
        self.assertIsInstance(schoolclass, SchoolClass)

