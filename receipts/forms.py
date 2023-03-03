from receipts.models import Receipt, ExpenseCategory
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


# feature 13
class ExpenseCategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
            'name',
        ]
