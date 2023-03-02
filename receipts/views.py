from django.shortcuts import render
from receipts.models import Receipt

# Create your views here.


def receipt(request):
    receipts = Receipt.objects.all()
    context = {
        'receipts': receipts,
    }
    return render(request, 'receipts/receipt.html', context)
