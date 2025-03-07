from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from nurse.forms import NurseForm, MedicalRecordForm
from nurse.models import Nurse, MedicalRecord
from nurse.serializers import NurseSerializer, MedicalrecordSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm



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
@api_view(['GET','POST'])
def nurseapi(request):
    if request.method == "GET":
        nurses = Nurse.objects.all()
        serializer = NurseSerializer(nurses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        serializer = NurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST'])
def medicalrecordapi(request):
    if request.method == "GET":
        medicalrecords = MedicalRecord.objects.all()
        serializer = MedicalrecordSerializer(medicalrecords, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        serializer = MedicalrecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})