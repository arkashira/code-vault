Generated `user-stories.md` for **code-vault** (overwrote a stale `cannabis-ops-sync` file left in `/tmp`).

**14 stories across 4 epics:**

1. **Tamper-Evident Vault** (3) — push-to-seal deposit, RFC 3161 timestamping, public Merkle anchoring. This is the defensibility core: provable *what existed, when*.
2. **Payment Gating & IP Transfer** (4) — milestone escrow terms, funded-gate-before-access, review window, scoped/staged release.
3. **Dispute Evidence & Proof-of-Delivery** (4) — signed PoD certificate, immutable case timeline, account-free verification, dispute freeze.
4. **Onboarding & Git-Native Workflow** (3) — real escrow provider integration, verified two-party invite, CI deposit hook.

Each story has 3–5 acceptance criteria and an S/M/L estimate. Distribution: **4 S / 6 M / 4 L**.

**Two opinionated calls baked in:**
- **MVP loop = US-1.1 + 1.2 + 2.2 + 3.1** — the minimum chain that proves the full hypothesis end to end (deposit → provable delivery → paid-before-handover → admissible evidence).
- **Scope discipline** — Epic 3 deliberately produces *exhibits*, not adjudication. That keeps us on the BD-identified "buildable, defensible sliver" (code-delivery escrow) and out of legal enforcement, which is neither buildable nor defensible for us.

One thing worth flagging for the architect/PRD step: US-1.2 and US-4.1 (TSA + real escrow provider) are the two `L` items carrying external-dependency and legal-admissibility risk — they should be de-risked with a spike before committing the milestone-gating logic on top.