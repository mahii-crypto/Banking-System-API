from django.urls import path

from .views import (
    RegisterView,
    CustomerListCreateView,
    CustomerDetailView,
    BankAccountListCreateView,
    BankAccountDetailView,
    TransactionListCreateView,
)

urlpatterns = [

    path("register/", RegisterView.as_view()),

    path("customers/", CustomerListCreateView.as_view()),
    path("customers/<int:pk>/", CustomerDetailView.as_view()),

    path("bank-accounts/", BankAccountListCreateView.as_view()),
    path("bank-accounts/<int:pk>/", BankAccountDetailView.as_view()),

    path("transactions/", TransactionListCreateView.as_view()),

]