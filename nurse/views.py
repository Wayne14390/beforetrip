from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from nurse.forms import NurseForm, MedicalRecordForm
from nurse.models import Nurse, MedicalRecord


# Create your views here.
def index(request):
    if request.method == "POST":
        form1 = NurseForm(request.POST, request.FILES)
        if form1.is_valid() :
            form1.save()

            return redirect('index')
    else:
        form1 = NurseForm()
    return render(request, 'index.html',{'form1': form1})


def medical(request):
    if request.method == "POST":
        form2 = MedicalRecordForm(request.POST)
        if  form2.is_valid():
            form2.save()
            return redirect('medical')
    else:
        form2 = MedicalRecordForm()
    return render(request, 'medical.html',{ 'form2': form2})

def nurselist(request):
    nurses = Nurse.objects.all()
    return render(request, 'nurselist.html',{'nurses': nurses})

def medicalrecordlist(request):
    medicalrecords = MedicalRecord.objects.all()
    return render(request, 'medicalrecordlist.html',{'medicalrecords': medicalrecords})

def editnurse(request, id):
    nurse = get_object_or_404(Nurse ,id=id)
    if request.method == "POST":
        form = NurseForm(request.POST,instance=nurse)
        if form.is_valid():
           form.save()
           return redirect('nurselist')
    else:
           form = NurseForm( instance=nurse)
    return render(request, 'editnurse.html',{'form': form, 'nurse': nurse})
def deletenurse(request, id):
    nurse = get_object_or_404(Nurse ,id=id)
    try:
        nurse.delete()
    except Exception as e:
        messages.error(request,'Nurse not deleted')
    return redirect('nurselist')

def editmedicalrecord(request, id):
    medicalrecord = get_object_or_404(MedicalRecord ,id=id)
    if request.method == "POST":
        form = MedicalRecordForm(request.POST,instance=medicalrecord)
        if form.is_valid():
           form.save()
           return redirect('medicalrecordlist')
    else:
           form = MedicalRecordForm( instance=medicalrecord)
    return render(request, 'editmedicalrecord.html',{'form': form, 'medicalrecord': medicalrecord})
def deletemedicalrecord(request, id):
    medicalrecord = get_object_or_404(Nurse ,id=id)
    try:
        medicalrecord.delete()
    except Exception as e:
        messages.error(request,'Record not deleted')
    return redirect('medicalrecordlist')