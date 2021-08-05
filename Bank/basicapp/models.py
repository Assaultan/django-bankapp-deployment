from django.db import models
from django.utils import timezone
# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    balance = models.IntegerField()

    def __str__(self):
        return self.name

class Transfers(models.Model):
    sender_name = models.ForeignKey(Customers, related_name='from_sender',on_delete=models.CASCADE)
    reciever_name = models.ForeignKey(Customers, related_name='to_reciever',on_delete=models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)
