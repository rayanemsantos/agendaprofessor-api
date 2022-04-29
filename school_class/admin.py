from django.contrib import admin
from .models import StudentSubject, StudentSubjectAverageGrade, ClassSubject, ClassSubjectHistory, ClassSubjectHistoryPresence
from django.utils.safestring import mark_safe
from django.urls import reverse

class StudentSubjectAverageGradeInlineAdmin(admin.StackedInline):
    model = StudentSubjectAverageGrade
    extra = 0

class EditLinkToInlineObject(object):
    def edit_link(self, instance):
        url = reverse('admin:%s_%s_change' % (
            instance._meta.app_label,  instance._meta.model_name),  args=[instance.pk] )
        if instance.pk:
            return mark_safe(u'<a href="{u}">edit</a>'.format(u=url))
        else:
            return ''

class MyModelInline(EditLinkToInlineObject, admin.TabularInline):
    model = ClassSubjectHistoryPresence
    readonly_fields = ('edit_link', )

# class ClassSubjectHistoryPresenceInlineAdmin(admin.StackedInline):
#     model = ClassSubjectHistoryPresence
#     extra = 0

class ClassSubjectHistoryInlineAdmin(admin.StackedInline):
    model = ClassSubjectHistory
    extra = 0
    inlines = (MyModelInline, )

class StudentSubjectAdmin(admin.ModelAdmin):
    model = StudentSubject
    inlines = (StudentSubjectAverageGradeInlineAdmin, )

class ClassSubjectHistoryAdmin(admin.ModelAdmin):
    model = ClassSubjectHistory
    inlines = (ClassSubjectHistoryInlineAdmin, )


admin.site.register(StudentSubject, StudentSubjectAdmin)
admin.site.register(ClassSubject, ClassSubjectHistoryAdmin)