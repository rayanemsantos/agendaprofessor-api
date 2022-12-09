from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ('full_name', 'serie', 'identification', 'shift', )


admin.site.register(Student, StudentAdmin)
