from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_accounts, name='list_accounts'),
    path('<uuid:account_id>/', views.account_detail, name='account_detail'),
    path('transfer/', views.transfer_funds, name='transfer_funds'),
    path('import/', views.import_accounts, name='import_accounts'),
]
