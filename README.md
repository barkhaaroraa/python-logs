# GitHub Actions Python Logging

This project demonstrates how to set up logging in a Python script and configure GitHub Actions for continuous integration, including log retention and failure alerts.

## Features

- Python script with logging and exception handling
- GitHub Actions workflow with log retention for 14 days
- Email alert for workflow failures using SMTP

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/github-actions-python-logging.git
   cd github-actions-python-logging
2.	Add Secrets to GitHub Repo
o	EMAIL_USERNAME: Your email (e.g., Gmail)
o	EMAIL_PASSWORD: App password
3.	Push to Main Branch
git add .
git commit -m "Initial commit"
git push origin main
4.	View Logs in GitHub Actions Go to the Actions tab in your GitHub repo to inspect log outputs.
Optional: GitHub CLI Logs
gh run list
gh run view <run-id> --log
