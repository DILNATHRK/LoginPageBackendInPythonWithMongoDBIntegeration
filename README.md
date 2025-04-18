# User Login Backend in Python with MongoDB Integration

This project demonstrates a user login system built using Python and MongoDB. The backend handles user registration, login, and authentication.

## Features

- User registration with email and password.
- Login functionality using stored credentials.
- MongoDB integration for storing user data.
- Built using Python and MongoDB.

## Requirements

- Python 3.x
- MongoDB (local or cloud instance)
- Flask (for the web framework)
- PyMongo (for MongoDB integration)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/DILNATHRK/LoginPageBackendInPythonWithMongoDBIntegeration.git
    ```

2. Navigate to the `userlogin` directory:
    ```bash
    cd LoginPageBackendInPythonWithMongoDBIntegeration/userlogin
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure MongoDB:
    - Make sure your MongoDB server is running, or use a MongoDB cloud service.
    - Update the connection string in the application configuration.

5. Run the application:
    ```bash
    python manage.py
    ```

## API Endpoints

- `POST /login`: Authenticate user with email and password.
- `POST /signup`: Register a new user with email and password.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
