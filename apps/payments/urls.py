from .views import MobileCommunicationCreateView, InternetPaymentCreateView, CommunalPaymentCreateView
from django.urls import path

urlpatterns=[
    path('mobilepayment/', MobileCommunicationCreateView.as_view(), name='mobilepayment'),
    path('internetpayment/', InternetPaymentCreateView.as_view(), name='internetpayment'),
    path('communalpayment/', CommunalPaymentCreateView.as_view(), name='communalpayment')
] 