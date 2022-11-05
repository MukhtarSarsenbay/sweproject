from django.contrib import admin
from . models import Patient
from . models import Doctor
# Register your models here.


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id_patient', 'IIN', 'email')


admin.site.register(Patient, PatientAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id_doctor', 'IIN', 'email', 'spec_id')


admin.site.register(Doctor, DoctorAdmin)