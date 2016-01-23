from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Account, Transaction
from django.core.urlresolvers import reverse


# Create your views here.
class AccountListView(ListView):
    model = Account


class AccountCreateView(CreateView):
    model = Account
    fields = ('name', 'balance', 'description')

    def get_success_url(self):
        return reverse("accounts:account_list")


class AccountUpdateView(UpdateView):
    model = Account
    fields = ('name', 'balance', 'description')

    def get_success_url(self):
        return reverse("accounts:account_list")


class AccountDeleteView(DeleteView):
    model = Account

    def get_success_url(self):
        return reverse("accounts:account_list")


class TransactionListView(ListView):
    model = Transaction

    def get_queryset(self):
        account_id = self.request.GET.get("account", None)
        return self.model.objects.all().filter(account__id=account_id)


class TransactionCreateView(CreateView):
    model = Transaction
    fields = ('account', 'notes', 'debit', 'credit')

    def get_form(self, form_class=None):
        account_id = self.request.GET.get("account", None)
        form = super(TransactionCreateView, self).get_form(form_class)

        if account_id:
            form.fields['account'].initial = account_id

        return form

    def get_success_url(self):
        account = self.request.POST.get("account")
        return reverse("accounts:transaction_list") + "?account=" + account


class TransactionDeleteView(DeleteView):
    model = Transaction

    def get_success_url(self):
        transaction = self.get_object()
        return reverse("accounts:transaction_list") + "?account=" + str(transaction.account.id)
