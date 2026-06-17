```markdown
# STORIES.md
_code-vault — User Story Backlog_

## Epic: Repository Intake & Integrity
*As a maintainer, I want to stakeholder repos in the vault with tamper-evident integrity guarantees so that downstream consumers can trust the origin and every byte.*

1. **As a developer, I want to push my GPL-licensed Rust library `iceoryx2` v0.9 source tree to the vault so that it becomes an immutable escrow record, stamped with a cryptographic Git commit hash and UTC timestamp.** *(migration from Lemmy thread)*
   - Acceptance Criteria:
     - CLI: `cv push --license gpl-3.0 --repo https://github.com/iceoryx2/iceoryx2 --tag v0.9 HEAD`
     - Vault stores exact tree + parents; generates on-chain proof receipt (BLAKE3 hash of every file > 128 KB, full git sha-1)
     - Output: `cv-receipt-{sha}.pdf` with embedded QR code linking to IPFS & Etherscan
     - `iceoryx2 Readme.md` included → vault records metadata.title = "iceoryx2 v0.9"

2. **As a compliance officer, I want the vault to automatically detect license conflicts (MIT, Apache-2.0, GPL-3.0, CDLA) within pushed repos so that we can flag risky dependencies before acceptance.**
   - Acceptance Criteria:
     - CI: scan `Cargo.lock`, `go.mod`, `package-lock.json`; if license mix violates whitelist return 409 with JSON diff
     - Whitelist cache refresh weekly via `license-scout` dataset (~9.4 M pairs)

3. **As a consumer, I want to verify an existing escrow item by its PDF receipt so that I can confirm the exact code snapshot without trusting the vault operator.**
   - Acceptance Criteria:
     - CLI: `cv verify --receipt cv-receipt-abc.pdf`
     - Output: `✅ Hash matches, valid since 2026-05-23T14:33:44Z, GPL-3.0 clean`
     - Fail fast on any modification: “❌ Tree hash mismatch — proof tampered.”

---

## Epic: Milestone Payment Release
*As a buyer, I want vault releases payment ONLY after deliverable acceptance, ensuring code is payment-validated.*

4. **As an escrow manager, I want to define milestones (e.g. v0.9 tag, README docs, tests) against a pushed repo so that payments unlock automatically on milestone completion.**
   - Acceptance Criteria:
     - Milestone JSON stored in vault metadata; keyed by tag
     - `cv milestone add --repo iceoryx2 --tag v0.9 --amount 5000USDC --acceptance tests-pass,Cargo-audit-clean`
     - Wallet integration on Polygon; release tx triggered via Chainlink oracle after QA pass (story 7)

5. **As a QA lead, I want a bot to run the iceoryx2 test suite inside an ephemeral Ubuntu container inside the vault CI so that I can auto-sign milestones when 100 % tests pass.**
   - Acceptance Criteria:
     - CLI: `cv qa --repo iceoryx2 --tag v0.9 --env ubuntu:24.04 --script "cargo test"`
     - Green run → milestone status updated `QA:PASSED`, CIjeta badge flips → triggers oracle unlock

---

## Epic: Access & Consumption
*As a consumer, I want safe, auditable access to vaulted deliverables once unlocked.*

6. **As a downstream user, I want to clone a payment-unlocked repo directly from the vault mirror so that I get the exact deliverable without any human red-tape.**
   - Acceptance Criteria:
     - CLI: `cv clone --receipt cv-receipt-abc.pdf --dest ./iceoryx2`
     - Mirror is read-only; IPFS CID verified against PDF; clone pulls only files allowed by license

7. **As a reviewer, I want every vault release to carry a dated review from a verified maintainer so that third-party audits can reference human judgment.**
   - Acceptance Criteria:
     - Review form: rating 1–5, short text, PGP-signed
     - `cv review add --receipt cv-receipt-abc.pdf --rating 5 --text "iceoryx2 meets robust IPC spec, passes 2x fuzz load"`
     - Automatically attached to PDF appendix; merkle root signed by reviewer’s key

---
## Epic: Self-Improvement & Growth
*As a system, I want to mine new escrow items from existing code vaults to extend our portfolio.*

8. **As the Axentx brain, I want to ingest every verified receipt into the shared pgvector BRAIN so that our scouting agent (HR/BD) can surface unmet demand by license type and domain.**
   - Acceptance Criteria:
     - Post-unlock, receipt metadata indexed into `surrogate-1-harvest` BRAIN vector store; embedding model = `sentence-transformers/all-MiniLM-L6-v2`, dimension 384
     - Queryable via: `mind search --license apache-2.0 --year 2026 --top 10`
     - Growth impact: added items ≤24 h lag

9. **As a product lead, I want to auto-generate suggested Stories for new repos landing in the vault so that we rapidly turn demand into validated features without duplication.**
   - Acceptance Criteria:
     - If repo topic matches existing portfolio (e.g., “IPC”, “scheduler”, “hypervisor”), AI agent drafts epics & stories using BRAIN context and license rules
     - Draft reviewed by PM within 1 h; auto-merge if non-duplicate with acceptance ≥ 80 % overlap in feature Jaccard
```
