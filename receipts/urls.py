from django.urls import path
from receipts.views import (receipt, create_receipt)


urlpatterns = [
    path('create/', create_receipt, name='create_receipt'),
    path('', receipt, name='home')
]
