# Planetarium Project

## Overview
This project is a RESTful API built with Django REST Framework (DRF). It provides endpoints for managing and retrieving data related to a planetarium, including shows, themes, and more.

## Getting Started

### Prerequisites
- Python 3.11 or higher
- Django 5.0 or higher
- Django REST Framework 3.12 or higher

### Installation
1. Clone the repository:
    ```bash
    git clone git@github.com:EugeneProtsenko/planetarium_project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd planetarium_project
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To run the server, use the following command:
```bash
python manage.py runserver
```

## Usage

After running the server with the command `python manage.py runserver`, the API will be available at `http://localhost:8000/`.

## API Endpoints

- `/api/planetarium`: You will see a list of all endpoints of the API

## Running Tests

To run the tests, use the following command:

```bash
python manage.py test
```

## API Documentation and Testing with Swagger

Also this project uses Swagger for API documentation and testing. Swagger provides a user-friendly, interactive interface for users to understand the API's endpoints, request/response types, status codes, etc.

From the Swagger UI, you can:

- View the list of endpoints in the API.
- Understand the purpose of each endpoint, the request method (GET, POST, PUT, DELETE, etc.), and the request/response format.
- Try out each endpoint directly from the UI.