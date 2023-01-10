from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, PatientDiagnostic, PatientIllness
from .forms import PatientForm
from django.urls import reverse

def home_page(request):
    return render(request, 'MHR/home.html')

def patient_form(request):
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_list')
    else:
        form = PatientForm()

    context = {'form': form}

    return render(request, 'MHR/patient_form.html', context)


def patients_list(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'MHR/patients_list.html', context)


def patient_details(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    context = {'patient': patient}
    return render(request ,'MHR/patient_details.html', context)

def update_patient_details(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=obj)

    if request.method == 'POST':
        print('z')
        if form.is_valid():
            form.save()
            return redirect(reverse('patient_details', args=[obj.pk]))

    context = {'obj': obj, 'form':form}
    return render(request, 'MHR/patient_form.html', context)

def delete_patient(request, pk):
    obj = get_object_or_404(Patient, pk=pk)
    obj.delete()
    return redirect('patients_list')