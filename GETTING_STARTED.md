Getting Started — Contributor Guide

Estimated onboarding time: ~45 minutes

This guide walks you from cloning the repository to submitting your first pull request using the project’s GitOps workflow.

Prerequisites

Ensure the following are installed:

Python ≥ 3.8 → python3 --version

Git → git --version

GitHub account

Code editor (VS Code recommended)

1. Clone the Repository
git clone https://github.com/Adenosine030/devops-capstone-gitops.git
cd devops-capstone-gitops
ls

Expected files: app.py, test_app.py, requirements.txt, etc.

2. Set Up Local Environment
Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip list

You should see flask, pytest, and flake8.

3. Verify Local Setup
Run application
python app.py

Service runs at:
http://127.0.0.1:5000

Test endpoints:

curl http://localhost:5000/health

curl -X POST http://localhost:5000/sum \
  -H "Content-Type: application/json" \
  -d '{"a":5,"b":10}'

curl -X POST http://localhost:5000/reverse-string \
  -H "Content-Type: application/json" \
  -d '{"text":"hello"}'

Stop with Ctrl+C.

Run tests
pytest -v

All tests should pass.

Run linting
flake8 app.py test_app.py --max-line-length=88

No output = success.

4. Workflow Overview
Trello flow

Backlog → In Progress → Review/QA → Done

Each task has ID TRELLO-###.

Branch naming
feature/TRELLO-###-short-description

Example:

feature/TRELLO-007-add-logging
Commit format
[TRELLO-###] Short description

Example:

[TRELLO-007] Add request logging middleware
5. First Contribution
Select task

Choose Trello card from Backlog

Move to In Progress

Note ID (e.g., TRELLO-007)

Create branch
git checkout main
git pull origin main
git checkout -b feature/TRELLO-###-description
Implement change

Edit relevant files and save.

Validate locally
pytest -v
flake8 app.py test_app.py --max-line-length=88

Fix all errors before committing.

Commit and push
git add .
git commit -m "[TRELLO-###] Description"
git push origin feature/TRELLO-###-description
Open Pull Request

Create PR on GitHub

Title: [TRELLO-###] Description

Wait for CI checks (green)

Merge when approved

Move Trello card → Done

Common Tasks
Run single test
pytest test_app.py::test_health -v
Add new test

Add to test_app.py:

def test_feature(client):
    res = client.post('/endpoint', json={"key": "value"})
    assert res.status_code == 200

Run:

pytest -v
Sync with main
git checkout main
git pull origin main
git checkout feature/TRELLO-###-description
git merge main

Resolve conflicts if prompted.

Troubleshooting
Missing modules
source venv/bin/activate
pip install -r requirements.txt
Tests failing locally
python3 --version
pip install -r requirements.txt --force-reinstall
rm -rf .pytest_cache
Lint errors
flake8 --show-source --max-line-length=88

Common fixes:

line length > 88

unused imports

missing blank lines

Git push authentication error

Use GitHub Personal Access Token instead of password.

CI fails on GitHub but not locally

Check Actions → failed job logs.
Most issues: missing files or uncommitted changes.

Best Practices

Never commit directly to main

Run tests before commit

One task per PR

Keep commits small and clear

Update Trello status continuously
