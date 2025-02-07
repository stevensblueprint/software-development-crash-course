# Software Development Crash Course

The goal of this workshop is to help you improve how you develop Software both independently, but especially as a TEAM. We are using a very simple Flask/Python web app to illustrate the concepts we will be discussing. The focus is not on writing the code itself, but on the process of developing the code.

## Prerequisites

- Have Python installed on your machine
- Have git installed on your machine and have a GitHub account

## Getting Started

1. Fork this repository
2. Clone the forked repository to your machine
3. Create a virtual environment
4. Install the dependencies
5. Run the project

6. Pick a task from the project board
7. Create a new branch following the naming convention `feature/your-feature-name`
8. Implement the feature
9. Push the branch to your forked repository

### Setting up Linting/Formatter

To run the formatter
```bash
black src/
```

To run the linter
```bash
pylint src/
```

**Note:** Make sure you have your virtual environment activated and you have installed all the dependencies from `requirements.txt`.

### Writing Tests with Pytest

PYTEST-SAMPLE

### Automating the Linting Checks and Tests with GitHub Actions
We want to make sure that on every pull request and push to main, we mantain the same coding standards.
To achieve this, GitHub has Github Actions. GitHub Actions is a CI/CD service that allows us to automate 
tasks within your software development lifecycle. It enables us to build, test, and deploy your code directly from GitHub.