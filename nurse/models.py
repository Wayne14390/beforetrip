from django.db import models

# Create your models here.
class Nurse(models.Model):
    image = models.ImageField(upload_to='nurse_images/',blank=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class MedicalRecord(models.Model):
    patient = models.CharField(max_length=20)
    doctor = models.CharField(max_length=20)
    diagnosis = models.TextField()
    prescription = models.TextField()
    visit_date = models.DateField()

    def __str__(self):
        return self.patient

class Doctor(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    Rank = models.CharField(max_length=20)
    ward = models.TextField()

    def __str__(self):
        return self.name

