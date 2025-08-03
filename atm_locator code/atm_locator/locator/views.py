from django.shortcuts import render, get_object_or_404
from .models import ATM

def atm_list(request):
    atms = ATM.objects.filter(is_functional=True, has_cash=True)
    return render(request, 'locator/atm_list.html', {'atms': atms})

def atm_detail(request, atm_id):
    atm = get_object_or_404(ATM, id=atm_id)
    return render(request, 'locator/atm_detail.html', {'atm': atm})
