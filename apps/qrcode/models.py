from django.db import models
from ..accounts.models import User, Accounts

import uuid
from django.utils import timezone
from dateutil import relativedelta


class QrCode(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    account=models.ForeignKey(Accounts, on_delete=models.CASCADE)
    qr_code=models.ImageField(upload_to='images')
    data=models.TextField(blank=True, null=True)
    STATUS=[
        ('active', 'Active'),
        ('used', 'Used'),
        ('expired', 'Expired')
    ]
    status=models.CharField(max_length=250, choices=STATUS)
    created_at=models.DateTimeField(auto_now_add=True)
    TYPE=[
        ('payment', 'Payement'),
        ('login', 'Login'),
        ('verification', 'Verification')
    ]
    type=models.CharField(max_length=50, choices=TYPE)
    qr_uuid=models.UUIDField(default=uuid.uuid4, unique=True, editable=False)

    def expire_date(self):
        return timezone.now() >= self.created_at+ relativedelta(years=1)
    
    def __str__(self):
        return f"{self.user} - {self.qr_code}"

