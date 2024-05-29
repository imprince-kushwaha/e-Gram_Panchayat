from django.contrib import admin

# Register your models here.
from egramApp.models import Aadhar,Birth,Death,Complaint,Contacts

admin.site.register(Aadhar)
admin.site.register(Birth)
admin.site.register(Death)
admin.site.register(Complaint)
admin.site.register(Contacts)
