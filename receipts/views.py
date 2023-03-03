from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from django.contrib.auth.decorators import login_required
from receipts.forms import ReceiptForm

# Create your views here.


@login_required
def receipt(request):
    receipts = Receipt.objects.filter(purchaser=request.user)
    context = {
        'receipts': receipts,
    }
    return render(request, 'receipts/receipt.html', context)


@login_required
def create_receipt(request):
    if request.method == 'POST':
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(commit=False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect('home')
    else:
        form = ReceiptForm()
    context = {
        'form': form,
    }
    return render(request, 'receipts/create_receipt.html', context)


# Feature 12 List Views


@login_required
def category_list(request):
    category = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        'receipts': category,
    }
    return render(request, 'receipts/category_list.html', context)


@login_required
def account_list(request):
    account = Account.objects.filter(owner=request.user)
    context = {
        'receipts': account,
    }
    return render(request, 'receipts/account_list.html', context)
