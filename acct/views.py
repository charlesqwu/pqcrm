from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#from django.http import Http404
#from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

#from django.http import HttpResponse
#from django.template import loader

from .models import AcctPayment


def payments(request, username):
    latest_payments = AcctPayment.objects.filter(uid=request.user.id).order_by('-created_at')[:100]
    context = {'latest_payments': latest_payments}
    return render(request, 'acct/payments.html', context)

def coupons(request, username):
    pass

def transactions(request, username):
    pass

