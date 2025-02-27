from django.contrib import admin

from nurse.models import Nurse, MedicalRecord, Doctor

# Register your models here.
admin.site.register(Nurse)
admin.site.register(MedicalRecord)
admin.site.register(Doctor)