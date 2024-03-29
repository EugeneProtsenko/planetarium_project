# Planetarium Project

The Planetarium Project is a Django REST-based project designed to manage and retrieve data related to a planetarium, including shows, themes, and more. This API allows you to get information about astronomy shows, show themes, and allows a registered user to purchase tickets.

## Features of the Project

- **Restriction of Information:** The information exchanged between the administrator and the regular user is restricted so that the user has access to only the information to which they are entitled.
- **Astronomy Show Information:** Get data on astronomy shows, including titles, descriptions, and show themes.
- **Ticket Information:** Allows authenticated users to check their orders and add tickets specifying a specific show to the order.
- **Authentication:** User can create a profile by entering email address and password. API is secured by JWT (JSON Web Tokens) authentication to protect sensitive data.

## Installation

### Prerequisites

- Install PostgreSQL and create a database
- Run the project locally without Docker

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/EugeneProtsenko/planetarium_project
    ```
2. Navigate to the project directory:
    ```bash
    cd planetarium_project
    ```
3. Create a virtual Python engine and activate it:
    ```bash
    python -m venv venv 
    source venv/bin/activate(on macOS)
    venv\Scripts\activate(on Windows)
    ```
4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
5. Rename a file name `.env_sample` to `.env` in the project root directory. Reconfirm that you have replaced all the keys of the middle with your real data:
    ```bash
    set POSTGRES_HOST=< db_host_name >
    set POSTGRES_NAME=< db_name >
    set POSTGRES_USER=< db_username >
    set POSTGRES_PASSWORD=< password_db >
    set SECRET_KEY=< secret_key >
    ```
6. Create database migrations:
    ```bash
    python manage.py migrate
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```
The API should now be accessible at `http://localhost:8001/`.

## Running with Docker

Docker should be installed

1. Build the Docker image:
    ```bash
    docker-compose build
    ```
2. Start the Docker container:
    ```bash
    docker-compose up
    ```

## Getting Access

1. Create a user at `api/user/register/`
2. Get an access token at `api/user/token/`
3. To authenticate, include the obtained token in your request headers with the format:
    ```bash
    Authorization: Bearer <your-token>
    ```

## API Documentation

To interact with the API using Swagger, open a web browser and navigate to `http://localhost:8001/api/schema/swagger/`. Here you will find detailed information about the available endpoints and how to use them.
