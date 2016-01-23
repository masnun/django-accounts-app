from django.conf.urls import patterns, url
from .views import AccountCreateView, AccountListView, AccountUpdateView, AccountDeleteView
from .views import TransactionCreateView, TransactionListView, TransactionDeleteView

accounts_urls = [

    url(r'^$', AccountListView.as_view(), name='account_list'),
    url(r'^create$', AccountCreateView.as_view(), name='account_create'),
    url(r'^update/(?P<pk>\d+)$', AccountUpdateView.as_view(), name='account_update'),
    url(r'^delete/(?P<pk>\d+)$', AccountDeleteView.as_view(), name='account_delete'),

    url(r'transaction/create$', TransactionCreateView.as_view(), name='transaction_create'),
    url(r'transaction/list$', TransactionListView.as_view(), name='transaction_list'),
    url(r'^transaction/delete/(?P<pk>\d+)$', TransactionDeleteView.as_view(), name='transaction_delete'),
]
