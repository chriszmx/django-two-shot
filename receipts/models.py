from django.db import models
from django.conf import settings


# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='categories')

    def __str__(self):
        return self.name


class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='accounts')


# class Receipt(models.Model):
#     vendor = models.CharField(max_length=200)
#     total = models.DecimalField(max_digits=10, decimal_places=3)
#     tax = models.DecimalField(max_digits=10, decimal_places=3)
#     date = models.DateTimeField()
#     purchaser = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                   on_delete=models.CASCADE,
#                                   related_name='receipts')
#     category = models.ForeignKey(ExpenseCategory,
#                                  on_delete=models.CASCADE,
#                                  related_name='receipts')
#     account = models.ForeignKey(Account,
#                                 on_delete=models.CASCADE,
#                                 related_name='receipts',
#                                 null=True)


# feature 14


class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name='accounts')

    # def __str__(self):
    #     return self.name


class Receipt(models.Model):
    vendor = models.CharField(max_length=200)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    tax = models.DecimalField(max_digits=10, decimal_places=3)
    date = models.DateTimeField()
    purchaser = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE,
                                  related_name='receipts')
    category = models.ForeignKey(ExpenseCategory,
                                 on_delete=models.CASCADE,
                                 related_name='receipts')
    account = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='receipts',
                                null=True)
