# from django.contrib import admin
# from .models import *
# # Register your models here.
# @admin.register(Recipe)
# class RecipeModelAdmin(admin.ModelAdmin):
#     list_display = ['id','receipe_name','receipe_description','receipe_image']

# @admin.register(Department)
# class DepartmentModelAdmin(admin.ModelAdmin):
#     list_display = ['department']

# @admin.register(StudentID)
# class StudentIDModelAdmin(admin.ModelAdmin):
#     list_display = ['student_id']

# @admin.register(Student)
# class StudentModelAdmin(admin.ModelAdmin):
#     list_display = ['department','student_id','student_name','student_email','student_age','student_address']


from django.contrib import admin
from .models import *
admin.site.register(Recipe)
admin.site.register(StudentID)
admin.site.register(Department)
@admin.register(Student)
class StudentModelAdmin(admin.ModelAdmin):
    list_display = ['department','student_id','student_name','student_email','student_age','student_address']

@admin.register(SubjectMarks)
class SubjectMarksModelAdmin(admin.ModelAdmin):
    list_display = ['get_student_id','student','subject','marks']

    def get_student_id(self, obj):
        return obj.student.student_id.student_id
    get_student_id.short_description = 'Student ID'

@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['subject_name']