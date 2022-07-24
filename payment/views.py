from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .import forms

from payment.models import Payment


# Create your views here.

def initiate_payment(request):
    
    return render(request, 'payment/initiate_payment.html', )



def makepayment(request):

    return render(request, 'payment/makepayment.html')

def verify_payment( request: HttpRequest, ref:str)-> HttpResponse:
    payment = get_object_or_404(Payment, ref=ref)
    verified = payment.verify_payment()
    if verified:
        messages.success(request, "verification Succcessful")
    else:
        messages.error(request, "verification Failed")
    return render(request, 'payment/initiatepayment.html', )
