from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db import transaction
from .models import Account
import csv
from io import TextIOWrapper
from decimal import Decimal, InvalidOperation
import uuid

def import_accounts(request):
    if request.method == "POST" and request.FILES.get("file"):
        file = TextIOWrapper(request.FILES["file"].file, encoding="utf-8")
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row

        success_count = 0
        error_count = 0
        error_details = []  # For storing error details

        for row in csv_reader:
            if len(row) < 3:
                error_count += 1
                error_details.append(f"Row {csv_reader.line_num}: Incomplete data")
                continue

            try:
                account_id = uuid.UUID(row[0].strip())
                name = row[1].strip()
                balance = row[2].strip().replace(",", "")
                balance = Decimal(balance)
            except (ValueError, InvalidOperation, uuid.UUIDError) as e:
                error_count += 1
                error_details.append(f"Row {csv_reader.line_num}: Invalid data. Error: {e}")
                continue

            try:
                account = Account.objects.create(id=account_id, name=name, balance=balance)
                success_count += 1
            except Exception as e:
                error_count += 1
                error_details.append(f"Row {csv_reader.line_num}: Failed to create account. Error: {e}")

        message = f"Imported {success_count} accounts successfully. {error_count} errors occurred."

        if error_count > 0:
            message += f"\nError details:\n" + "\n".join(error_details)

        return redirect('list_accounts')

    return render(request, "accounts/import_accounts.html")

def list_accounts(request):
    accounts = Account.objects.all()
    return render(request, "accounts/list_accounts.html", {"accounts": accounts})

def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    return render(request, "accounts/account_detail.html", {"account": account})

@transaction.atomic
def transfer_funds(request):
    if request.method == "POST":
        from_account_id = request.POST["from_account"]
        to_account_id = request.POST["to_account"]
        amount = Decimal(request.POST["amount"])

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
