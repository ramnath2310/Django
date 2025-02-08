from django.db import models

class Employee(models.Model):
    basic_info = models.OneToOneField('BasicInformation', on_delete=models.CASCADE, null=True, blank=True)
    education_details = models.OneToOneField('EducationDetails', on_delete=models.CASCADE, null=True, blank=True)
    previous_work = models.OneToOneField('PreviousWork', on_delete=models.CASCADE, null=True, blank=True)
    bank_details = models.OneToOneField('BankDetails', on_delete=models.CASCADE, null=True, blank=True)
    

class BasicInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    is_fresher = models.BooleanField(default=False)

class EducationDetails(models.Model):
    institution_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    graduation_year = models.IntegerField()

class PreviousWork(models.Model):
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class BankDetails(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    ifsc_code = models.CharField(max_length=11)
