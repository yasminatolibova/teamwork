from django.contrib import admin

# Register your models here.
from .models import PaymentType, Status, MobileCommunication, InternetPayment, CommunalPayment

admin.site.register(PaymentType)
admin.site.register(Status)
admin.site.register(MobileCommunication)
admin.site.register(InternetPayment)
admin.site.register(CommunalPayment)
