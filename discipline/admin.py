from django.contrib import admin

from .models import Discipline, RegisterStudent

class RegisterStudentAdmin(admin.ModelAdmin):
    list_filter = ['discipline']

admin.site.register(RegisterStudent, RegisterStudentAdmin)
admin.site.register(Discipline)
