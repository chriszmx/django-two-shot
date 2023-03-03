from receipts.models import Receipt
from django.forms import ModelForm


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = ['vendor',
                  'total',
                  'tax',
                  'date',
                  'category',
                  'account',
                  ]
