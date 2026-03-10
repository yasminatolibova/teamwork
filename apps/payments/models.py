from django.db import models
from ..accounts.models import User, Accounts
import uuid
# Create your models here.

class PaymentType(models.Model):
    types=models.CharField(max_length=250)
    def __str__(self):
        return self.types

class Status(models.Model):
    status=models.CharField(max_length=250)
    def __str__(self):
        return self.status

class MobileCommunication(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    COMPANIES=[
        ('beeline', 'Beeline'),
        ('ucell', 'Ucell'),
        ('uzmobile', 'UzMobile'),
        ('mobiuz', 'MobiUz'),
        ('humans', 'Humans'),
        ]
    operator=models.CharField(max_length=20, choices=COMPANIES)
    phone_number=models.CharField(max_length=15)
    account=models.ForeignKey(Accounts, on_delete=models.CASCADE)
    operator_account_number=models.CharField(max_length=50, blank=True, null=True)
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    commission=models.DecimalField(max_digits=4, decimal_places=2)
    type=models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    current_balance=models.DecimalField(max_digits=15, decimal_places=2, default=0)
    debt=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    transaction_id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    tarif_nomi=models.CharField(max_length=250, blank=True, null=True)

    def total_amount(self):
        return self.amount+self.amount*self.commission/100
    
    def __str__(self):
        return f"{self.phone_number}"



class InternetPayment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    PROVIDER=[
        ('uztelecom', 'Uztelecom'),
        ('sarkor telecom', 'Sarkor Telecom'),
        ('turon telecom', 'Turon Telecom'),
        ('tps', 'TPS'),
        ('sharq telecom', 'Sharq Telecom'),
        ('comnet', 'Comnet'),
        ('east telecom', 'East Telecom'),
        ('iplus', 'IPLUS'),
        ('nano telecom', 'Nano Telecom'),
       ( 'free link', 'Free link')
    ]
    provider=models.CharField(max_length=250, choices=PROVIDER)
    provider_account_number=models.CharField(max_length=50, blank=True, null=True)
    price=models.DecimalField(max_digits=8, decimal_places=2)
    commission=models.DecimalField(max_digits=4, decimal_places=2)
    type=models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    account=models.ForeignKey(Accounts, on_delete=models.CASCADE)
    current_balance=models.DecimalField(max_digits=15, decimal_places=2, default=0)
    debt=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    transaction_id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


    def total_price(self):
        return self.price+self.price*self.commission/100
    def __str__(self):
        return f"{self.total_price()}"


class CommunalPayment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    SERVICE_TYPE=[
        ('elektr energiyasi', 'Elektr Energiyasi'),
        ('ichimlik suvi', 'Ichimlik Suvi'),
        ('tabiiy gaz', 'Tabiiy Gaz'),
        ('issiqlik energiyasi', 'Issiqlik Energiyasi'),
        ('kanalizatsiya', 'Kanalizatsiya'),
        ('chiqindi', 'Chiqindi')
    ]
    PROVIDER=[
        ('hududgaz', 'Hududgaz'),
        ('regional electric networks', 'Regional Electric Networks(RES)'),
        ("suvta'minot", "Suvta'minot"),
        ('toza hudud', 'Toza Hudud'),
        ("issiqlik ta'minoti", "Issiqlik ta'minoti")

    ]
    provider=models.CharField(max_length=250, choices=PROVIDER)
    provider_account_number=models.CharField(max_length=50, blank=True, null=True)
    service_type=models.CharField(max_length=50, choices=SERVICE_TYPE)
    account=models.ForeignKey(Accounts, on_delete=models.CASCADE)
    current_balance=models.DecimalField(max_digits=15, decimal_places=2, default=0)
    debt=models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    cost=models.DecimalField(max_digits=20, decimal_places=2)
    commission=models.DecimalField(max_digits=4, decimal_places=2)
    type=models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    status=models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    transaction_id=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)


    def total_cost(self):
        return self.cost+self.cost*self.commission/100
    
    def __str__(self):
        return f"{self.total_cost()}"


    