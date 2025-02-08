from django import forms
from .models import BasicInformation, EducationDetails, PreviousWork, BankDetails

class BasicInformationForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = BasicInformation
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address', 'date_of_birth','is_fresher']
class EducationDetailsForm(forms.ModelForm):
    class Meta:
        model = EducationDetails
        fields = ['institution_name', 'degree', 'graduation_year']

class PreviousWorkForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}))
    class Meta:
        model = PreviousWork
        fields = ['company_name', 'job_title', 'start_date', 'end_date']

class BankDetailsForm(forms.ModelForm):
    class Meta:
        model = BankDetails
        fields = ['bank_name', 'account_number', 'ifsc_code']
