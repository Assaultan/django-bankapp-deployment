from django.shortcuts import render
from django.http import HttpResponse
from basicapp.models import Customers,Transfers
from . import forms
# Create your views here.

def homepage(request):
    return render(request,'basicapp/base.html')

def customers(request):
    cust_list = Customers.objects.order_by('name')
    cust_dict = {'custs':cust_list}
    return render(request,'basicapp/index.html',context=cust_dict)

def transferForm(request):
    form = forms.TransferForm()
    if request.method == 'POST':
        form = forms.TransferForm(request.POST)
        if form.is_valid():
            amt=int(form.cleaned_data['amount'])
            sender=str(form.cleaned_data['sender_name'])
            reciever=str(form.cleaned_data['reciever_name'])
            try:
                send=Customers.objects.get(name=sender)
                got=Customers.objects.get(name=reciever)
                print("Success")
            except:
                msg="<b>Your sender or reciever doesn't match with our bank enter valid names</b>"
                return HttpResponse(msg)
            if amt<0:
                msg2="<b>Please enter positive amount</b> "
                return HttpResponse(msg2)
            elif send.balance < amt:
                msg3="<b>Insufficient Fund</b>"
                return HttpResponse(msg3)
            if send==got:
                msg4="<b>Sender and Reciever Should be different</b>"
                return HttpResponse(msg4)
            if (send.balance-amt) > 0 and amt>0:
                send.balance-=amt
                send.save(update_fields=['balance'])
                got.balance+=amt
                got.save(update_fields=['balance'])
                form.save()
                return transfers(request)
    return render(request,'basicapp/form.html',{'form':form})


def transfers(request):
    transfer_list = Transfers.objects.order_by('date')
    transfer_dict = {'trans':transfer_list}
    return render(request,'basicapp/transfers.html',context=transfer_dict)
