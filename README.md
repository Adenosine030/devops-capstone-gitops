DevOps Capstone — GitOps Workflow & CI Automation

Project Overview

This project demonstrates a professional GitOps workflow integrating task tracking (Trello), version control (GitHub), and automated CI (GitHub Actions). It enforces industry-standard practices including feature branching, automated testing, linting, and merge protection to prevent defective code from reaching the main branch.

The repository simulates how a small engineering team maintains code quality, traceability, and workflow visibility in a modern DevOps environment.

Architecture

Stack

Flask — REST API

Pytest — automated testing

Flake8 — code quality

GitHub Actions — CI pipeline

Trello — task tracking

Git/GitHub — source control

Endpoints

GET /health — service health

POST /sum — numeric addition with validation

POST /reverse-string — string reversal with type checks

GitOps Workflow

Key principles implemented:

Git as single source of truth

Trello-linked development (TRELLO-###)

Feature branch workflow

Pull-request based merges

Automated CI quality gates

Traceable commits and tasks

Trello flow

Backlog → In Progress → Review/QA → Done

Each feature branch and commit references its Trello card for end-to-end traceability.

Commit Convention
[TRELLO-###] Short imperative description

Example:

[TRELLO-002] Add input validation for sum endpoint

This convention links planning (Trello) to implementation (Git), enabling traceability, auditing, and release tracking.

CI/CD Pipeline

Triggered on pushes and pull requests to main and feature/**.

Stages:

Install dependencies

Lint (Flake8)

Tests (Pytest)

Quality enforcement:

Lint failure → block merge

Test failure → block merge

All checks must pass before PR merge

Development Workflow

Create Trello card

Create feature/TRELLO-### branch

Commit using Trello ID

Open PR

CI validation

Merge after success

Full onboarding: GETTING_STARTED.md
Contribution guide: CONTRIBUTING.md

Reflection Questions
Q1 — Branching Strategy

A feature-branch workflow (feature/TRELLO-###) was used to isolate work, enable parallel development, and maintain traceability to requirements. Each change is developed independently and validated through CI before integration, reducing risk to the main branch.

Including the Trello ID in branch names provides instant context during reviews and debugging. This model scales well across teams because it preserves clean history, controlled merges, and task-linked development.

Q2 — Preventing Bad Code Merges

Merge protection is achieved through automated CI enforcement. GitHub Actions runs linting and tests on every push and pull request. Any failure blocks merge approval, ensuring only validated code reaches main.

This removes reliance on manual checks and provides immediate feedback to developers. The automated pipeline acts as a consistent quality gate, enforcing standards regardless of time pressure or human error.

Q3 — Scaling to 30 Engineers

At larger scale, additional controls would be required:

Branch protection rules (required checks & approvals)

CODEOWNERS-based reviews

Parallelized CI for speed

Multi-environment deployments (dev/staging/prod)

Release branches and feature flags

More advanced work tracking (Jira-style)

The core GitOps principles remain unchanged, but governance and automation depth increase to manage coordination and risk.

Q4 — DevOps & Operations Learning

This project demonstrated that modern operations is primarily automation and feedback systems rather than manual infrastructure work. CI pipelines embed operational safeguards directly into development, ensuring reliability by default.

Fast feedback loops, infrastructure-as-code pipelines, and automated enforcement reduce risk while increasing delivery speed. DevOps culture also shifts responsibility left — developers consider deployment, monitoring, and rollback during implementation rather than after release.

Q5 — Trello–Git Correlation

Commits reference Trello IDs ([TRELLO-###]), creating a direct link between requirements and code. This enables traceability from planning to implementation, simplifying audits, debugging, release notes, and status tracking.

The correlation also supports process improvement by showing effort per task and change history. This structured linkage scales across teams and enables automation such as PR-to-task tracking and workflow reporting.

Project Metrics

Commits: 15+

Pull Requests: 3+

Tests: 10+

Trello Cards: 5+

CI Runs: 20+

Repository Structure
devops-capstone-gitops/
├── .github/workflows/ci.yml
├── app.py
├── test_app.py
├── requirements.txt
├── GETTING_STARTED.md
├── CONTRIBUTING.md
└── README.md
Author

Ademola Adenigba
DevOps Engineering — Axia Africa
Capstone Project · 2026
