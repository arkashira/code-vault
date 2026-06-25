import pytest
import hashlib
import json
from code_vault import CodeVault, VaultEntry

def test_create_vault_entry():
    code_vault = CodeVault()
    repository_state = "example repository state"
    vault_entry = code_vault.create_vault_entry(repository_state)
    assert vault_entry.repository_state == repository_state
    assert vault_entry.hash == hashlib.sha256(repository_state.encode()).hexdigest()

def test_get_vault_entry():
    code_vault = CodeVault()
    repository_state = "example repository state"
    vault_entry = code_vault.create_vault_entry(repository_state)
    retrieved_vault_entry = code_vault.get_vault_entry(vault_entry.hash)
    assert retrieved_vault_entry == vault_entry

def test_update_vault_entry():
    code_vault = CodeVault()
    repository_state = "example repository state"
    vault_entry = code_vault.create_vault_entry(repository_state)
    with pytest.raises(ValueError):
        code_vault.update_vault_entry(vault_entry.hash, "new repository state")

def test_display_vault_entry():
    code_vault = CodeVault()
    repository_state = "example repository state"
    vault_entry = code_vault.create_vault_entry(repository_state)
    displayed_vault_entry = code_vault.display_vault_entry(vault_entry.hash)
    assert json.loads(displayed_vault_entry) == vault_entry.__dict__

def test_display_non_existent_vault_entry():
    code_vault = CodeVault()
    with pytest.raises(ValueError):
        code_vault.display_vault_entry("non_existent_hash")
