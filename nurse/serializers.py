from rest_framework import serializers

from nurse.models import Nurse, MedicalRecord


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = ['name','age','gender','date_of_birth']

class MedicalrecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['patient','doctor','diagnosis','prescription','visit_date']
