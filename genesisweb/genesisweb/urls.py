from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from website import views
from django.conf.urls import url
from django.conf import settings
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'^$', views.Homeview, name='home'),
    url('admin/', admin.site.urls),
    url(r'^application', views.Applicantview, name='applicant'),
    url('^edit/(?P<pk>\d+)/$', views.EditApplicantView.as_view(), name='editapplicant'),
    url('delete/(?P<pk>\d+)/$',views.DeleteApplicantView.as_view(), name='deleteapplicant'),
    url('^edit/(?P<pk>\d+)/$', views.EditDisbursementView.as_view(), name='editdisbursement'),
    url('delete/(?P<pk>\d+)/$',views.DeleteDisbursementView.as_view(), name='deletedisbursement'),
    url(r'^disbursement', views.Disbursementview, name='disbursement'),
    url(r'^viewapplication', views.showapplicantsview, name='applicantslist'),
    url(r'^viewdisbursements', views.viewdisbursements, name='disbursementview'),
    url(r'^myaccounts', views.myaccountview, name='myaccount'),
    url(r'^resetpass', views.resetpasswordview, name='resetpassword'),
    url(r'^codetesting', views.testview, name='tester'),
    url(r'^extracode', views.extracodeview, name='extracode'),
    url(r'^blog', views.blogview, name='blog'),
    url(r'^drugandalcoholdetox', views.drugandalcoholdetoxview, name='drugandalcoholdetox'),
    url(r'^contactus', views.contactusview, name='contactus'),
    url(r'^treatment', views.treatmentview, name='treatment'),
    url(r'^locations', views.locationsview, name='locations'),
    url(r'^detox', views.detoxview, name='detox'),
    url(r'^aboutus', views.aboutusview, name='aboutus'),
    url(r'^learnmore', views.learnmoreview, name='learnmore'),
    url(r'^aftercare', views.aftercareview, name='aftercare'),
    url(r'^gallery', views.galleryview, name='gallery'),
    url(r'^signatureservices', views.signatureservicesview, name='signatureservices'),
    url(r'^signatureservices2', views.signatureservices2view, name='signatureservices2'),
    url(r'^ocdanxiety', views.ocdanxietyview, name='ocdanxiety'),
    url(r'^traumaresilience', views.traumaresilienceview, name='traumaresilience'),
    url(r'^formlogin', views.loginformview, name='loginform'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

