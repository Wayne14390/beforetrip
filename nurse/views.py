from django.shortcuts import render, redirect

from nurse.forms import NurseForm, MedicalRecordForm


# Create your views here.
def index(request):
    if request.method == "POST":
        form1 = NurseForm(request.POST)
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


