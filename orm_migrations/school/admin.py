from django.contrib import admin

from .models import Student, Teacher, StudentPosition


class PositionInline(admin.TabularInline):
    model = StudentPosition


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    inlines = [PositionInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')


# @admin.register(StudentTeacher)
# class StudentTeacherAdmin(admin.ModelAdmin):
#     list_display = ('student', 'teacher')