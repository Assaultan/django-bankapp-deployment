from django.forms import models
from django.shortcuts import render
from django.http import HttpResponse
from basicapp.models import Customers,Transfers
from django.urls import reverse_lazy
from . import forms
from basicapp.forms import TransferForm
from django.views.generic.edit import FormView
from django.views.generic import(TemplateView,
                                 ListView,DetailView,
                                 CreateView,UpdateView,
                                 DeleteView)
                                 
# Create your views here.


class IndexView(TemplateView):
    template_name='basicapp/basicapp_base.html'

class CustomerDetailView(DetailView):
    context_object_name='customer_detail'
    model=Customers
    template_name='basicapp/customer_detail.html'

class CustomersListView(ListView):
    context_object_name='customer'
    model=Customers

class CustomerCreateView(CreateView):
    fields=('name','email','balance')
    model=Customers

class CustomerUpdateView(UpdateView):
    fields=('name','balance')
    model=Customers

class CustomerDeleteView(DeleteView):
    model=Customers
    success_url=reverse_lazy("basic_app:customers")


class TransfersListView(ListView):
    context_object_name='transfer'
    model=Transfers    
    ordering = ['date']

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
    return render(request,'basicapp/transfer_form.html',{'form':form})


def transfers(request):
    transfer_list = Transfers.objects.order_by('date')
    transfer_dict = {'trans':transfer_list}
    return render(request,'basicapp/transfers_list.html',context=transfer_dict)



class CustomerCreateView(CreateView):
    model=Customers
    fields=('name','email','balance')
    
