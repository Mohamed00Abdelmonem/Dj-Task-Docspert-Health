from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db import transaction
from .models import Account
import csv
from io import TextIOWrapper

from django.shortcuts import render
from django.http import JsonResponse
import csv
from io import TextIOWrapper
from .models import Account

def import_accounts(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = TextIOWrapper(request.FILES["file"].file, encoding="utf-8")
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row if present

        for row in csv_reader:
            if len(row) < 2:
                # Log or handle rows with insufficient data
                continue
            name = row[0]
            try:
                balance = float(row[1])
            except ValueError:
                # Log or handle rows with invalid balance data
                continue
            Account.objects.create(name=name, balance=balance)
        return JsonResponse({"message": "Accounts imported successfully"})
    return render(request, "accounts/import_accounts.html")

# List All Accounts
def list_accounts(request):
    accounts = Account.objects.all().values("id", "name", "balance")
    return JsonResponse(list(accounts), safe=False)

# Get Account Information
def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return JsonResponse({"id": account.id, "name": account.name, "balance": account.balance})

# Transfer Funds
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db import transaction
from .models import Account
from decimal import Decimal
@transaction.atomic
def transfer_funds(request):
    if request.method == "POST":
        from_account_id = request.POST["from_account"]
        to_account_id = request.POST["to_account"]
        amount = Decimal(request.POST["amount"])  # Convert amount to Decimal

        from_account = get_object_or_404(Account, id=from_account_id)
        to_account = get_object_or_404(Account, id=to_account_id)

        if from_account.balance < amount:
            return JsonResponse({"error": "Insufficient funds"}, status=400)

        from_account.balance -= amount
        to_account.balance += amount

        from_account.save()
        to_account.save()

        return JsonResponse({"message": "Transfer successful"})

    return render(request, "accounts/transfer_funds.html")
