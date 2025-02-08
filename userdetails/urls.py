from django.urls import path
from .views import basic_information_view, education_details_view, previous_work_view, bank_details_view, success_view

urlpatterns = [
    path('', basic_information_view, name='basic_information'),
    path('education-details/<int:basic_info_id>/', education_details_view, name='education_details'),
    path('previous-work/<int:basic_info_id>/', previous_work_view, name='previous_work'),
    path('bank-details/<int:basic_info_id>/', bank_details_view, name='bank_details'),
    path('success/', success_view, name='success'),
]
