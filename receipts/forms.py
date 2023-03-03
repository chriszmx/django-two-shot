from receipts.models import Receipt, ExpenseCategory, Account
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


# feature 14


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'name',
            'number',
        ]
