from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import MobileCommunicationSerializer, InternetPaymentSerializer, CommunalPaymentSerializer
from .models import MobileCommunication, InternetPayment, CommunalPayment



class MobileCommunicationCreateView(generics.CreateAPIView):
    queryset=MobileCommunication.objects.all()
    serializer_class=MobileCommunicationSerializer
    permission_classes=[IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InternetPaymentCreateView(generics.CreateAPIView):
    queryset=InternetPayment.objects.all()
    serializer_class=InternetPaymentSerializer
    permission_classes=[IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommunalPaymentCreateView(generics.CreateAPIView):
    queryset=CommunalPayment.objects.all()
    serializer_class=CommunalPaymentSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
