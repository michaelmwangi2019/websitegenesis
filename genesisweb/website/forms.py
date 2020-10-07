from django import forms
from .models import Applicationtable, Disbursementtable


class Applicationform(forms.ModelForm):
    class Meta:
        model = Applicationtable
        widgets = {'Application_Date': forms.DateInput(format=('%m/%d/%Y'),
                                                        attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                               'type': 'date'}), }
        fields = ['First_Name', 'Middle_Name', 'Last_Name', 'Gender', 'Applicant_ID', 'Amount', 'Birth_Date', 'Guardian_Telephone', 'Institution_Name', 'Application_Date']


class Disbursementform(forms.ModelForm):
    class Meta:
        model = Disbursementtable
        widgets = {'Disbursement_Date': forms.DateInput(format=('%m/%d/%Y'),
                                                        attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                               'type': 'date'}), }
        fields = ['Applicant_ID', 'Amount_Disbursed', 'Disbursement_No', 'Disbursement_Date']
