from django.contrib import admin

# Register your models here.
from .models import Applicationtable, Disbursementtable
admin.site.register(Applicationtable)
admin.site.register(Disbursementtable)
