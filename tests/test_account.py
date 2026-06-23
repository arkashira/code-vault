import pytest
from account import Account, AccountManager

def test_account_creation() -> None:
    manager = AccountManager()
    account = manager.create_account(1)
    assert account.tier == "free"
    assert account.escrows == 0

def test_account_upgrade() -> None:
    manager = AccountManager()
    account = manager.create_account(1)
    manager.upgrade_account(1)
    assert account.tier == "paid"

def test_create_escrow_free_tier() -> None:
    manager = AccountManager()
    account = manager.create_account(1)
    account.create_escrow()
    account.create_escrow()
    with pytest.raises(ValueError):
        account.create_escrow()

def test_create_escrow_paid_tier() -> None:
    manager = AccountManager()
    account = manager.create_account(1)
    manager.upgrade_account(1)
    for _ in range(5):
        account.create_escrow()
    assert account.escrows == 5
