from django.test import TestCase
from decimal import Decimal
from .models import Account

class AccountModelTest(TestCase):
    def setUp(self):
        """Set up test data"""
        Account.objects.create(name="John Doe", balance=Decimal('100.0'))
        Account.objects.create(name="Jane Smith", balance=Decimal('200.0'))

    def test_account_creation(self):
        """Test that accounts are created correctly"""
        john = Account.objects.get(name="John Doe")
        jane = Account.objects.get(name="Jane Smith")
        self.assertEqual(john.balance, Decimal('100.0'))
        self.assertEqual(jane.balance, Decimal('200.0'))

    def test_transfer_funds(self):
        """Test transferring funds between accounts"""
        john = Account.objects.get(name="John Doe")
        jane = Account.objects.get(name="Jane Smith")
        amount = Decimal('50.0')  # Ensure amount is a Decimal

        # Transfer funds from John to Jane
        john.balance -= amount
        jane.balance += amount
        john.save()
        jane.save()

        # Refresh from database
        john.refresh_from_db()
        jane.refresh_from_db()

        self.assertEqual(john.balance, Decimal('50.0'))
        self.assertEqual(jane.balance, Decimal('250.0'))
