Project file structure.

GitHub Workflow: .github/workflows/checks.yml
This file defines a workflow named Checks for automating the testing and linting of the project.

name: Checks
Purpose: The name of the workflow as displayed in the GitHub Actions interface.
Description: It helps identify the workflow among other workflows in the repository.

on: [push]
Purpose: Specifies when the workflow should run.
Description: In this case, the workflow runs every time there is a push event to the repository. You can modify this to include other events like pull_request or scheduled runs.

Jobs Definition
jobs:
  test-lint:
    name: Test Lint
    runs-on: ubuntu-latest
Purpose: Defines a job named test-lint that runs on the ubuntu-latest environment provided by GitHub Actions.
Description: This is the main job for running tests and linting code. All subsequent steps are part of this job.

Step 1: Login to Docker Hub
- name: Login to Docker Hub
  uses: docker/login-action@v2
  with:
    username: ${{ secrets.DOCKERHUB_USER }}
    password: ${{ secrets.DOCKERHUB_TOKEN }}
Purpose: Logs into Docker Hub using credentials stored as GitHub Secrets.
Description: Allows the workflow to pull or push Docker images securely. Replace DOCKERHUB_USER and DOCKERHUB_TOKEN with appropriate secret keys configured in the GitHub repository settings.

Step 2: Checkout the Repository
- name: Checkout
  uses: actions/checkout@v2
Purpose: Checks out the project repository to the GitHub Actions runner.
Description: This step ensures the runner has access to the repository files for subsequent steps.

Step 3: Run Tests
- name: Test
  run: docker compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test"
Purpose: Runs the test suite for the project using Docker Compose.
Description:
python manage.py wait_for_db: Ensures the database is ready before running tests.
python manage.py test: Executes the Django test suite to validate code correctness.

Step 4: Run Linter
- name: Lint
  run: docker compose run --rm app sh -c "flake8"

Project File Structure
Below is the file structure with explanations to help your classmate continue implementing the project:

project-root/
│
├── .github/
│   └── workflows/
│       └── checks.yml         # Defines GitHub Actions workflow for testing and linting.
│
├── app/
│   ├── Dockerfile             # Specifies how to build the Docker image for the app.
│   ├── requirements.txt       # Lists Python dependencies required for the project.
│   ├── manage.py              # Django's command-line utility for administrative tasks.
│   └── app/                   # Main Django application directory.
│       ├── __init__.py        # Indicates that this is a Python package.
│       ├── settings.py        # Django project settings.
│       ├── urls.py            # URL configuration for the app.
│       ├── models.py          # Database models for the app.
│       ├── views.py           # Views defining the app's logic.
│       └── tests.py           # Test cases for the app.
│
├── docker-compose.yml         # Defines and runs multi-container Docker applications.
├── .env                       # Example environment variables configuration.
├── .flake8                    # Configuration file for the Flake8 linter.
├── README.md                  # Provides an overview and setup instructions for the project.
└── LICENSE                    # License information for the project.


