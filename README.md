
# Python_NourishNow_Project

# Author: Kipngenoh Aaron

This is a Flask-based web application for managing user donations and articles. It allows users to create accounts, make cash or food donations, write articles, and view their donation and article history. The application uses SQLAlchemy to interact with a SQLite database.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Routes and Endpoints](#routes-and-endpoints)
- [Database Models](#database-models)
- [Usage Examples](#usage-examples)
  - [Adding a User](#adding-a-user)
  - [Adding Cash Donation](#adding-cash-donation)
  - [Adding Food Donation](#adding-food-donation)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

Follow these steps to get the Flask application up and running:

1. Clone the repository to your local machine:
   ```shell
   git clone git@github.com:kipngenohaaron/Python_NourishNow_Project.git
   cd Python_NourishNow_Project
   ```

2. Create a virtual environment (optional but recommended):
   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
   ```

3. Install the required dependencies:
   ```shell
   pip install -r requirements.txt
   ```

4. Initialize the SQLite database:
   ```shell
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Start the Flask application:
   ```shell
   flask run
   ```

6. Access the application in your web browser at `http://localhost:5000`.

## Features

- User registration and authentication.
- Cash and food donation functionality.
- Article creation and retrieval.
- Viewing user donation and article history.
- A simple home page.

## Routes and Endpoints

- `/` (Home Page)
- `/signUp` (User Registration)
- `/signIn` (User Authentication)
- `/donateFunds/<int:id>` (Add Cash Donation)
- `/donateFood/<int:id>` (Add Food Donation)
- `/userDonations/<int:id>` (View User's Donations)
- `/articles` (Create Article)
- `/articles/user/<int:user_id>` (View User's Articles)
- `/articles/<int:article_id>` (View Specific Article)

## Database Models

### User Model

- `id` (Primary key and unique identifier)
- `name` (User's name)
- `email` (User's email address, unique)
- `password` (User's password)
- Relationships:
  - `donations` (One-to-many relationship with `Donation` model)
  - `articles` (One-to-many relationship with `Article` model)

### Donation Model

- `id` (Primary key and unique identifier)
- `user_id` (Foreign key referencing the `User` model)
- `type` (Type of donation, e.g., "Cash" or "Food")
- `amount` (Donation amount or quantity)
- `date` (Date and time of the donation, defaulting to the current UTC time)

### Article Model

- `id` (Primary key and unique identifier)
- `user_id` (Foreign key referencing the `User` model)
- `author` (Author's name, can be the same as the user's name)
- `title` (Title of the article)
- `body` (Content of the article as text)

## Usage Examples

### Adding a User

To add a user to your Flask application, send a POST request to the `/signUp` endpoint. Here's an example using Postman:

1. Open Postman.

2. Create a new request by clicking the "New" button.

3. Choose the HTTP request type as "POST."

4. Set the request URL to `http://localhost:5000/signUp`.

5. Add a request header:
   - Key: `Content-Type`
   - Value: `application/json`

6. In the request body, provide JSON data with the user's registration information. For example:
   ```json
   {
       "name": "Kipngenoh",
       "email": "kipngenohaaron@gmail.com",
       "password": "secret_password"
   }
   ```

7. Click the "Send" button.

8. Postman will display the response from your Flask application, including details of the newly registered user, such as the user ID, name, and email.

### Adding Cash Donation

To add a cash donation to your Flask application, send a POST request to the `/donateFunds/<int:id>` endpoint. Here's an example using Postman:

1. Open Postman.

2. Create a new request by clicking the "New" button.

3. Choose the HTTP request type as "POST."

4. Set the request URL to an appropriate endpoint for adding cash donations, such as `http://localhost:5000/donateFunds/1` (Replace `1` with the desired user ID).

5. Add a request header:
   - Key: `Content-Type`
   - Value: `application/json`

6. In the request body, provide JSON data with the cash donation amount. For example:
   ```json
   {
       "amount": 100
   }
   ```

7. Click the "Send" button.

8. Postman will display the response from your Flask application, including details of the cash donation, such as the donation ID, user ID, type (Cash), donation amount, and date.

### Adding Food Donation

To add a food donation to your Flask application, send a POST request to the `/donateFood/<int:id>` endpoint. Here's an example using Postman:

1. Open Postman.

2. Create a new request by clicking the

 "New" button.

3. Choose the HTTP request type as "POST."

4. Set the request URL to an appropriate endpoint for adding food donations, such as `http://localhost:5000/donateFood/2` (Replace `2` with the desired user ID).

5. Add a request header:
   - Key: `Content-Type`
   - Value: `application/json`

6. In the request body, provide JSON data with the food donation details, including the number of food items. For example:
   ```json
   {
       "amount": 10
   }
   ```

7. Click the "Send" button.

8. Postman will display the response from your Flask application, including details of the food donation, such as the donation ID, user ID, type (Food), donation amount (number of food items), and date.

You can use Postman to simulate user interactions with your Flask application's donation features by sending POST requests with different user IDs and donation amounts as needed.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

# Contacts
### Email Address: kipngenohaaron@gmail.com
#### Phone Number: 0724 828197 / 0724279400


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.