# HelloUserAPI

The project is a simple API designed to manage user data with basic CRUD operations. Additionally, it includes a special route for generating personalized greeting messages.

---

### *Core Features*

1. *User Management API*:
    - *Add a User*:
        - Endpoint: POST /users
        - Description: Adds a new user to the database.
    - *List All Users*:
        - Endpoint: GET /users
        - Description: Retrieves a list of all users.
    - *Get User by ID*:
        - Endpoint: GET /users/{id}
        - Description: Fetches details of a user by their unique ID.
    - *Update User*:
        - Endpoint: PUT /users/{id}
        - Description: Updates the details of a specific user by ID.
    - *Delete User*:
        - Endpoint: DELETE /users/{id}
        - Description: Deletes a user by their unique ID.
2. *Greeting Message API*:
    - *Personalized Greeting*:
        - Endpoint: GET /greet_user/{id}/
        - Description: Fetches user details from the database and generates a personalized greeting message based on the user’s name.