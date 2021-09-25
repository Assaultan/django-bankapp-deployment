from django.db import models
from django.db.models.deletion import DO_NOTHING, SET_DEFAULT, SET_NULL
from django.urls import reverse
from django.http import HttpResponse
from django.utils import timezone
# Create your models here.

class Customers(models.Model):
    name = models.CharField(max_length=30,unique=True)
    email = models.EmailField(unique=True)
    balance = models.IntegerField()

    def get_absolute_url(self):
        return reverse('basicapp:detail',kwargs={'pk':self.pk})
        
    def __str__(self):
        return self.name

class Transfers(models.Model):
    sender_name = models.ForeignKey(Customers, related_name='from_sender',on_delete= models.CASCADE)
    reciever_name = models.ForeignKey(Customers, related_name='to_reciever',on_delete= models.CASCADE)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)
