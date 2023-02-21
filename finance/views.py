

from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from accounts.models import UserBankAccount



def index(request):
    return render(request, "finance/index.html", {})


def transfer_form(request):
    return render(request, "finance/transfer_form.html", {})

def search(request, form=None):
    try:
        if request.method == 'GET':
            query = request.GET.get('query')
            if query:
                accounts = UserBankAccount.objects.filter(account_no=query).get()
                return render(request, "finance/search.html", {
                    'query': query,
                    'accounts': accounts,
                })
    except ObjectDoesNotExist:
       return HttpResponse("<p>Invalid account please enter valid account number</p>")



def success(request):
    return render(request, 'finance/success.html')






