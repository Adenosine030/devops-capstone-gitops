Contributing Guide

Thank you for contributing to the DevOps Capstone project.
This document defines the development workflow, coding standards, and quality gates that ensure consistent, traceable, and reliable contributions.

Development Workflow

All work follows the GitOps lifecycle:

Trello → Branch → Code → Local Validation → Commit → PR → CI → Merge → Trello Done
Steps

Select Trello card from Backlog

Move to In Progress and assign yourself

Create feature branch

Implement change + tests

Validate locally (tests + lint)

Commit using Trello ID

Push and open PR

CI must pass

Merge to main

Move Trello card → Done

Branching Strategy
Naming Convention
feature/TRELLO-###-short-description

Examples:

feature/TRELLO-007-add-logging
feature/TRELLO-008-fix-validation
feature/TRELLO-009-update-docs
Rules

lowercase with hyphens

include Trello ID

≤ 50 characters

one task per branch

never commit directly to main

Commit Convention
Format
[TRELLO-###] Short imperative description

Optional body:

[TRELLO-007] Add request logging

- Log request/response metadata
- Add request ID correlation
- Improve observability
Requirements

Trello ID required

imperative tense (“Add”, “Fix”, “Update”)

concise and specific

no WIP or vague messages

Pull Request Process
Before Opening PR

tests pass locally

lint passes

branch up to date with main

commits follow convention

PR Title
[TRELLO-###] Short description
PR Description Template
## Description
What changed and why

## Changes
- key modifications

## Validation
- tests added/updated
- tested locally

## Trello
TRELLO-###
Merge Conditions

A PR may be merged only when:

CI pipeline passes

no merge conflicts

scope matches Trello card

Testing Standards

All new functionality must include tests.

Test Pattern
def test_feature(client):
    payload = {"a": 5, "b": 10}
    res = client.post("/sum", json=payload)
    assert res.status_code == 200
Commands
pytest -v
pytest test_app.py::test_health -v
Code Quality Standards
Style

PEP 8 compliant

max line length: 88

4-space indentation

2 blank lines between functions

descriptive names

Linting
flake8 app.py test_app.py --max-line-length=88

Zero lint errors required before PR.

CI Pipeline

CI enforces quality automatically.

Stages

Dependency install

Lint (flake8)

Tests (pytest)

Triggers

push to main

pull request to main

push to feature/**

Results

✅ pass → merge allowed

❌ fail → merge blocked

Handling Failures
Lint Errors
flake8 --show-source --max-line-length=88

Fix and re-run until clean.

Test Failures
pytest -v

Fix code or tests before commit.

Merge Conflicts
git checkout main
git pull origin main
git checkout feature/TRELLO-###-description
git merge main

Resolve conflicts, commit, push.

Contribution Principles

small, focused changes

test before commit

one task per PR

keep history traceable

automate quality checks

keep main stable

Need Help?

open GitHub issue

team communication channel

project mainta
