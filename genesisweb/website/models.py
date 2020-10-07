from django.db import models
# Create your models here.


class Applicationtable(models.Model):
    First_Name = models.CharField(max_length=50, null=False)
    Middle_Name = models.CharField(max_length=50, null=False)
    Last_Name = models.CharField(max_length=50, null=False)
    Gender = models.CharField(max_length=6, null=False)
    Applicant_ID = models.IntegerField(unique=True)
    Amount = models.IntegerField(null=False)
    Birth_Date = models.DateField(null=False)
    Guardian_Telephone = models.IntegerField(null=False, default=0)
    Institution_Name = models.CharField(max_length=254, null=True)
    Application_Date = models.DateField(null=False)

    def __str__(self):

        return self.First_Name


class Disbursementtable(models.Model):
    Applicant_ID = models.ForeignKey(Applicationtable, on_delete=models.PROTECT)
    Amount_Disbursed = models.IntegerField(null=False)
    Disbursement_No = models.IntegerField(unique=True)
    Disbursement_Date = models.DateField(null=False)

    #def __str__(self):

        #return self.Applicant_ID


class Contactustable(models.Model):
    fname = models.CharField(max_length=50, null=False)
    phonenum = models.IntegerField(unique=True)
    county = models.CharField(max_length=50, null=False)
    subject = models.CharField(max_length=254, null=True)
    hearus = models.CharField(max_length=254, null=True)

    #def __str__(self):

        #return self.phonenum

