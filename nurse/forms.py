from django import forms

from nurse.models import Nurse, MedicalRecord


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
