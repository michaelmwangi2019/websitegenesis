from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
from .forms import Applicationform, Disbursementform
from .models import Applicationtable, Disbursementtable
from .models import Contactustable
from django.http import HttpResponse


def Homeview(request):

    return render(request, 'home.html')


def Applicantview(request):
    form = Applicationform(request.POST)
    if form.is_valid():
        form.save()
    form = Applicationform()
    context = {'form': form}
    return render(request, 'Applicant.html', context)


def Disbursementview(request):
    form = Disbursementform(request.POST)
    if form.is_valid():
        form.save()
    form = Disbursementform()
    context = {'form': form}
    return render(request, 'Disbursement.html', context)


def Contactusview(request):
    form = Contactusform(request.POST)
    if form.is_valid():
        form.save()
    form = Contactusform()
    context = {'form': form}
    return render(request, 'viewcontactus.html', context)


def showapplicantsview(request):
    Applicants = Applicationtable.objects.all()
    return render(request, 'viewApplicants.html', {'Applicants': Applicants})


def viewdisbursements(request):
    Disbursements = Disbursementtable.objects.all()
    return render(request, 'viewDisbursements.html', {'Disbursements': Disbursements})


def viewcontactus(request):
    Contactus = Contactustable.objects.all()
    return render(request, 'viewcontactus.html', {'contactus': Contactus})


def testview(request):

    return render(request, 'codetesting.html')


def blogview(request):

    return render(request, 'blog.html')

def contactusview(request):

    return render(request, 'contactus.html')


def treatmentview(request):

    return render(request, 'treatment.html')


def aboutusview(request):

    return render(request, 'aboutus.html')


def detoxview(request):

    return render(request, 'detox.html')


def locationsview(request):

    return render(request, 'locations.html')


def blogview(request):

    return render(request, 'blog.html')


def signatureservicesview(request):

    return render(request, 'signatureservices.html')

def signatureservices2view(request):

    return render(request, 'signatureservices2.html')


def ocdanxietyview(request):

    return render(request, 'ocdanxiety.html')


def traumaresilienceview(request):

    return render(request, 'traumaresilience.html')


def eatingdisorderview(request):

    return render(request, 'eatingdisorder.html')


def galleryview(request):

    return render(request, 'gallery.html')


def extracodeview(request):

    return render(request, 'extracode.html')


def learnmoreview(request):

    return render(request, 'learnmore.html')


def aftercareview(request):

    return render(request, 'aftercare.html')


def myaccountview(request):

    return render(request, 'my_account.html')


def resetpasswordview(request):

    return render(request, 'resetpassword.html')


def loginformview(request):

    return render(request, 'loginform.html')


class EditApplicantView(UpdateView):
    model = Applicationtable
    fields = ('First_Name', 'Middle_Name', 'Last_Name', 'Gender', 'Applicant_ID', 'Amount', 'Birth_Date',
              'Guardian_Telephone', 'Institution_Name', 'Application_Date')
    template_name = 'editApplicant.html'
    success_url = reverse_lazy('applicantslist')

    def form_valid(self, form):
        post = form.save(commit=False)

        post.save()
        return redirect('applicantslist')


class EditDisbursementView(UpdateView):
    model = Disbursementtable
    fields = ('Applicant_ID', 'Amount_Disbursed', 'Disbursement_No', 'Disbursement_Date')
    template_name = 'editDisbursement.html'
    success_url = reverse_lazy('Disbursements')

    def form_valid(self, form):
        post = form.save(commit=False)

        post.save()
        return redirect('Disbursements')


class DeleteApplicantView(DeleteView):
    model = Applicationtable
    template_name = 'deleteApplicant.html'
    success_url = reverse_lazy('applicantslist')


class DeleteDisbursementView(DeleteView):
    model = Applicationtable
    template_name = 'deleteDisbursement.html'
    success_url = reverse_lazy('disbursementslist')



#contact us form
