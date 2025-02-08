from django.shortcuts import render, redirect, get_object_or_404
from .forms import BasicInformationForm, EducationDetailsForm, PreviousWorkForm, BankDetailsForm
from .models import BasicInformation, EducationDetails, PreviousWork


def basic_information_view(request):
    if request.method == 'POST':
        form = BasicInformationForm(request.POST)
        if form.is_valid():
            basic_info = form.save()
            return redirect('education_details', basic_info_id=basic_info.id)
    else:
        form = BasicInformationForm()
    return render(request, 'basic_information.html', {'form': form})

def education_details_view(request, basic_info_id):
    basic_info = get_object_or_404(BasicInformation, id=basic_info_id)
    if request.method == 'POST':
        form = EducationDetailsForm(request.POST)
        if form.is_valid():
            education_detail = form.save(commit=False)
            education_detail.basic_info = basic_info
            education_detail.save()
            return redirect('previous_work', basic_info_id=basic_info.id)
    else:
        form = EducationDetailsForm()
    return render(request, 'education_details.html', {'form': form, 'basic_info_id': basic_info_id})

def previous_work_view(request, basic_info_id):
    basic_info = get_object_or_404(BasicInformation, id=basic_info_id)
    is_fresher = basic_info.is_fresher
    if request.method == 'POST':
        if is_fresher:
            return redirect('bank_details', basic_info_id=basic_info.id)
        form = PreviousWorkForm(request.POST)
        if form.is_valid():
            previous_work = form.save(commit=False)
            previous_work.basic_info = basic_info
            previous_work.save()
            return redirect('bank_details', basic_info_id=basic_info.id)
    else:
        form = PreviousWorkForm()
    return render(request, 'previous_work.html', {'form': form, 'basic_info_id': basic_info_id,'is_fresher': is_fresher})

def bank_details_view(request, basic_info_id):
    basic_info = get_object_or_404(BasicInformation, id=basic_info_id)
    success_msg =''
    if request.method == 'POST':
        form = BankDetailsForm(request.POST)
        if form.is_valid():
            bank_detail = form.save(commit=False)
            bank_detail.basic_info = basic_info
            bank_detail.save()
            success_msg = 'All the details saved successfully!'
            form=None
            
    else:
        form = BankDetailsForm()
    return render(request, 'bank_details.html', {'form': form, 'basic_info_id': basic_info_id,'success_message': success_msg})

def success_view(request):
    return render(request, 'success.html')
