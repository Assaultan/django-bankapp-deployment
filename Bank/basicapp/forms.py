from django import forms
from django.core import validators
from basicapp.models import Customers,Transfers

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfers
        fields = ("sender_name","reciever_name","amount")























"""
def clean(self):
    all_clean_data=super().clean()
    sender_name = all_clean_data['Sender']
    reciever_name = all_clean_data['Reciever']
    amount = all_clean_data['Amount']

    if sender == reciever:
        raise forms.ValidationError("Sender and Reciever should be different")
    if amt < 1:
        raise forms.ValidationError("Amount should be Positive")

    class Meta():
        model = Transfers
        fields = ("sender_name","sender_name","amount","date")
"""
    # Sender = forms.CharField()
    # Reciever = forms.CharField()
    # Amount = forms.IntegerField()
    # botcatcher = forms.CharField(required=False,
    #                             widget=forms.HiddenInput,
    #                             validators=[validators.MaxLengthValidator(0)])
    # def clean(self):
    #     all_clean_data=super().clean()
    #     sender_name = all_clean_data['Sender']
    #     reciever_name = all_clean_data['Reciever']
    #     amount = all_clean_data['Amount']
    #
    #     if sender_name == reciever_name:
    #         raise forms.ValidationError("Sender and Reciever should be different")
    #     if amount < 1:
    #         raise forms.ValidationError("Amount should be Positive")
