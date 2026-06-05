# Contributing to Omni-Sentinel

First off, thank you for considering contributing to Omni-Sentinel! It is people like you who make the cognitive execution environment safer for everyone.

## Security First

Given the nature of this project (AGI/ASI Governance), **security is our top priority**.

If you discover a security vulnerability, please do **not** open an issue. Instead, please follow our Security Disclosure Policy:
1. Email the core team at `security@onefinestarstuff.org` (hypothetical).
2. Wait for a confirmation from the team.
3. We follow coordinated disclosure practices.

## How Can I Contribute?

### Reporting Bugs
- Use the GitHub Issue Tracker.
- Describe the steps to reproduce the bug.
- Include information about your environment (Python version, OS, etc.).

### Suggesting Enhancements
- Open a feature request in the Issue Tracker.
- Explain the "why" and "how" the enhancement aligns with the [Master Roadmap](SENTINEL_G_MASTER_ROADMAP_2026_2035.md).

### Pull Requests
1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes (`python3 -m pytest tests/`).
5. All code must follow the principles in `AGENTS.md` (if present) and maintain PQC compliance.

## Styleguides

### Git Commit Messages
- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Reference issues and pull requests liberally after the first line.

### Python Code Style
- Follow PEP 8.
- Use `secrets.SystemRandom()` for all randomness.
- Ensure all sensitive data handling is PQC-ready.

## Community

Join our (hypothetical) Discord or mailing list to discuss the future of ASI alignment!
