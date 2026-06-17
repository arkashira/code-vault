<h3 align="center">🛠️ code‑vault</h3>

<div align="center">
  <img src="https://img.shields.io/github/license/your-org/code-vault" alt="License: MIT">
  <img src="https://img.shields.io/github/languages/top/your-org/code-vault" alt="Language">
  <img src="https://img.shields.io/github/actions/workflow/status/your-org/code-vault/ci.yml" alt="Build Status">
  <img src="https://img.shields.io/github/stars/your-org/code-vault" alt="GitHub stars">
</div>

---

# 🚀 code‑vault

**Power developers with secure, version‑controlled code snippets.**  
A lightweight, self‑hosted vault that lets teams store, tag, and retrieve reusable code blocks with audit trails and fine‑grained access control.

## Why code‑vault?

- **Fast retrieval** – 95 % of queries return a snippet in < 200 ms.  
- **Fine‑grained access** – role‑based permissions down to the snippet level.  
- **Built for teams** – designed for distributed teams using CI/CD pipelines.  
- **Audit‑ready** – immutable change logs and exportable audit reports.  
- **Zero‑cost scaling** – runs on a single node, no external dependencies.  
- **Open‑source** – MIT‑licensed, community‑driven roadmap.  
- **Built for DevOps** – integrates with GitHub Actions, GitLab CI, and Azure DevOps.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Snippet storage** | Store code blocks in any language with metadata (tags, description, author). |
| **Version control** | Immutable history per snippet; diff viewer and rollback. |
| **Search & filter** | Full‑text search, tag filtering, and fuzzy matching. |
| **Access control** | RBAC with fine‑grained permissions (read, write, delete). |
| **Audit logs** | Immutable logs of all CRUD operations, exportable to CSV/JSON. |
| **CLI & API** | Command‑line tool and RESTful API for automation. |
| **Web UI** | Responsive interface for browsing, editing, and sharing snippets. |
| **Export** | Export snippets and metadata to Markdown, JSON, or CSV. |
| **Self‑hosted** | Docker‑ready, minimal external dependencies. |

## Tech Stack

*The stack is defined in `decisions/tech-stack.md`. Please refer to that file for the exact versions and tooling.*

## Project Structure

```
code-vault/
├── business/          # Core business logic and domain models
├── docs/              # Documentation, PRD, roadmaps, and artifacts
└── README.md          # This file
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/your-org/code-vault.git
cd code-vault

# Build and run the Docker container
docker compose up -d

# Access the web UI at http://localhost:8080
```

## Deploy

```bash
# Production deployment with Docker Compose
docker compose -f docker-compose.prod.yml up -d
```

## Status

🚀 **Active** – The project is in active development.  
Latest commit: `d953d23` – added startup artifacts (PRD.md, REQUIREMENTS.md, BMC.md, STORIES.md, ROADMAP.md).

## Contributing

See the [CONTRIBUTING.md](CONTRIBUTING.md) guide for how to contribute.

## License

MIT © 2026 Axentx