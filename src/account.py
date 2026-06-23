from dataclasses import dataclass
from typing import Optional

@dataclass
class Account:
    id: int
    tier: str = "free"
    escrows: int = 0

    def can_create_escrow(self) -> bool:
        if self.tier == "free" and self.escrows >= 2:
            return False
        return True

    def upgrade(self) -> None:
        self.tier = "paid"

    def create_escrow(self) -> None:
        if self.can_create_escrow():
            self.escrows += 1
        else:
            raise ValueError("Cannot create more escrows")

class AccountManager:
    def __init__(self) -> None:
        self.accounts = {}

    def create_account(self, id: int) -> Account:
        account = Account(id)
        self.accounts[id] = account
        return account

    def get_account(self, id: int) -> Optional[Account]:
        return self.accounts.get(id)

    def upgrade_account(self, id: int) -> None:
        account = self.get_account(id)
        if account:
            account.upgrade()
