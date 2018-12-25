from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

#from django.http import Http404
#from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

#from django.http import HttpResponse
#from django.template import loader

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import AcctPayment, AcctTransaction


def payments(request, username):
    all_payments = AcctPayment.objects.filter(uid=request.user.id).order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(all_payments, 100)
    try:
        payments_list = paginator.page(page)
    except PageNotAnInteger:
        payments_list = paginator.page(1)
    except EmptyPage:
        payments_list = paginator.page(paginator.num_pages)
    context = {'payments_list': payments_list}
    return render(request, 'acct/payments.html', context)





def coupons(request, username):
    pass


def transactions(request, username):
    latest_transactions = AcctTransaction.objects.filter(uid=request.user.id).order_by('-created_at')[:100]
    context = {'latest_transactions': latest_transactions}
    return render(request, 'acct/transactions.html', context)    
    

