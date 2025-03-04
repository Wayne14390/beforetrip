from django import forms

from nurse.models import Nurse, MedicalRecord


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Enter your age'}),
            'gender': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your gender'}),
            'date_of_birth':forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Enter your date of birth'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                       'accept':'image/*',
                       'title':'Select your image'
                       }
            ),
            }

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        widgets = {
            'patient': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your patient'}),
            'doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your doctor'}),
            'diagnosis': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your diagnosis'}),
            'prescription': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your prescription'}),
            'visit_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Enter your date of visit'}),
        }
