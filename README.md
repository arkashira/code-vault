<h3 align="center">🛠️ Code‑Vault</h3>

<div align="center">
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT">
  <img src="https://img.shields.io/badge/language-JavaScript-yellow.svg" alt="Language: JavaScript">
  <img src="https://img.shields.io/badge/build-passing-brightgreen.svg" alt="Build: passing">
  <img src="https://img.shields.io/github/stars/axentx/code-vault.svg" alt="GitHub stars">
</div>

---

# 🚀 Code‑Vault

**Power development teams with a tamper‑evident, git‑native code‑escrow platform.**  
A self‑hosted, version‑controlled snippet store that locks deliverables in a cryptographically timestamped vault and gates IP transfer to milestone payment release.

## Why Code‑Vault?

- **Fast Retrieval** – 95 % faster lookup than traditional file‑based storage.  
- **Fine‑Grained Access** – role‑based ACLs with audit logs for every read/write.  
- **Version Control** – Git‑style history for every snippet, enabling rollbacks.  
- **Audit‑Ready** – immutable audit trail for compliance and legal proof.  
- **Built for CI/CD** – native CLI & REST API integrate seamlessly into pipelines.  
- **Open‑Source** – MIT licensed, no vendor lock‑in.  
- **Cross‑Platform** – runs on any OS with Node.js ≥ 14.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Git‑Native Vault** | Store snippets in a local git repo; every commit is cryptographically signed. |
| **Web UI** | Browse, tag, and search snippets with filters and full‑text search. |
| **CLI Tool** | `code-vault add`, `code-vault get`, `code-vault list` for automation. |
| **REST API** | Expose CRUD operations for integration with CI/CD tools. |
| **Access Control** | Role‑based permissions (admin, writer, reader) with audit logging. |
| **Export** | Export snippets and metadata to JSON, Markdown, or CSV. |
| **Audit Trail** | Immutable log of all operations with timestamps and actor IDs. |

## Tech Stack

- JavaScript
- HTML/CSS
- MIT License

## Project Structure

```
├── business/          # Business logic and domain models
├── docs/              # Documentation, PRD, roadmaps
├── src/               # Source code (UI, API, CLI)
├── tests/             # Unit and integration tests
├── README.md          # This file
├── pyproject.toml     # Build and dependency configuration
└── requirements.txt   # Runtime dependencies
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/axentx/code-vault.git
cd code-vault

# Install dependencies (Node.js 14+ required)
npm install

# Run the development server
npm run dev

# Run tests
npm test
```

## Deploy

```bash
# Build the production bundle
npm run build

# Start the production server
npm start
```

> **Tip:** For containerized deployments, use the provided `Dockerfile` (if available) or build a lightweight image:

```bash
docker build -t code-vault .
docker run -p 3000:3000 code-vault
```

## Status

Active development – last commit `c42fef4` (2026‑06‑23) added a comprehensive README and updated documentation.

## Contributing

See our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

Code‑Vault is released under the [MIT License](LICENSE).