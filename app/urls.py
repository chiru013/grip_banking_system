from django.urls import path
from .views import usersList, sendMoney , handleTransfer, transactions, home , search

urlpatterns = [
    path('' , usersList , name='userlist' ),
    path('home' , home , name='home' ),
    path('transactions' , transactions , name='transactions' ),
    path('handletransfer' , handleTransfer , name='handletransfer' ),
    path('search' , search , name='handletransfer' ),
    path('sendmoney/<int:id>' , sendMoney , name='sendmoney' ),

]