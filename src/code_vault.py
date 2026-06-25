import hashlib
import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class VaultEntry:
    repository_state: str
    hash: str

class CodeVault:
    def __init__(self):
        self.vault = {}

    def create_vault_entry(self, repository_state: str) -> VaultEntry:
        hash_object = hashlib.sha256(repository_state.encode())
        hash_hex = hash_object.hexdigest()
        vault_entry = VaultEntry(repository_state, hash_hex)
        self.vault[hash_hex] = vault_entry
        return vault_entry

    def get_vault_entry(self, hash_hex: str) -> VaultEntry:
        return self.vault.get(hash_hex)

    def update_vault_entry(self, hash_hex: str, new_repository_state: str) -> None:
        if hash_hex in self.vault:
            raise ValueError("Vault is immutable")
        else:
            raise ValueError("Vault entry not found")

    def display_vault_entry(self, hash_hex: str) -> str:
        vault_entry = self.get_vault_entry(hash_hex)
        if vault_entry:
            return json.dumps(vault_entry.__dict__)
        else:
            raise ValueError("Vault entry not found")
