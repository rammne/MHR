from django.contrib import admin
from .models import Patient, PatientDiagnostic, PatientIllness

admin.site.register(Patient)
admin.site.register(PatientDiagnostic)
admin.site.register(PatientIllness)
