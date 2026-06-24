<h3 align="center">🛠️ Code-Vault</h3>

<div align="center">
  <a href="https://github.com/axentx/code-vault/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/badge/License-MIT-blue.svg" />
  </a>
  <a href="https://github.com/axentx/code-vault">
    <img alt="Language" src="https://img.shields.io/badge/Language-Python-blue.svg" />
  </a>
  <a href="https://github.com/axentx/code-vault/actions/workflows/main.yml">
    <img alt="Build" src="https://github.com/axentx/code-vault/actions/workflows/main.yml/badge.svg" />
  </a>
  <a href="https://github.com/axentx/code-vault/stargazers">
    <img alt="Stars" src="https://img.shields.io/github/stars/axentx/code-vault" />
  </a>
</div>

---
# 🚀 Code-Vault
**Power development teams with secure code snippet management.** Code-Vault is a self-hosted, version-controlled code snippet store for development teams with tamper-evident and git-native features.

## Why Code-Vault?
* **Secure**: Tamper-evident and git-native features ensure the integrity of your code snippets.
* **Version-controlled**: Track changes to your code snippets with ease.
* **Self-hosted**: Keep your code snippets on your own servers, with full control over access and security.
* **Fine-grained access control**: Control who can access and modify your code snippets.
* **Immutable audit trail**: Keep a record of all changes to your code snippets.
* **Fast retrieval**: Quickly retrieve the code snippets you need.
* **Integration with CI/CD tools**: Use our REST API to integrate Code-Vault with your CI/CD tools.

## Feature Overview
| Feature | Description |
| --- | --- |
| Code Snippet Storage | Store code snippets in a local git repository |
| Web UI | Access and manage code snippets through a web interface |
| CLI Tool | Manage code snippets from the command line |
| REST API | Integrate Code-Vault with CI/CD tools |
| Access Control | Control who can access and modify code snippets |
| Export Options | Export code snippets in various formats |
| Immutable Audit Trail | Keep a record of all changes to code snippets |

## Tech Stack
* Python
* HTML/CSS
* Git

## Project Structure
* `business`: Business logic and models
* `docs`: Documentation and startup artifacts
* `src`: Source code for the web UI, CLI tool, and REST API
* `tests`: Unit tests and integration tests

## Getting Started
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python src/main.py
```

## Deploy
```bash
# Build the Docker image
docker build -t code-vault .

# Run the Docker container
docker run -p 8080:8080 code-vault
```

## Status
Last commit: `9cdb82b` - style: [DECISION] docs cycle 20260624-154234-code-vau

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License
Code-Vault is licensed under the MIT License. See [LICENSE](LICENSE) for more information.