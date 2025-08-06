# AWS Lambda + API Gateway + DynamoDB User API

This project is a simple serverless REST API built using **AWS Lambda**, **API Gateway**, and **DynamoDB**. It demonstrates how to create and retrieve users via HTTP requests using AWS services.

## 🧰 Tech Stack

- **AWS Lambda** – Backend logic (Python)
- **API Gateway** – RESTful API layer
- **DynamoDB** – NoSQL database for storing user data
- **Python 3.12** – Lambda runtime
- **AWS Cloud9** – Development environment

---

## 🚀 Features

- `POST /user`: Add a new user (name, email, class)
- `GET /users`: Retrieve all users stored in the database

---

## 📂 API Endpoints

### ➕ POST `/user`

**Add a user to DynamoDB**

#### Request
```bash
curl -X POST https://your-api-url/dev/user \
  -H "Content-Type: application/json" \
  -d '{
        "name": "Alice",
        "email": "alice@example.com",
        "class": "5th"
      }'

### Response
{
  "message": "User added successfully"
}

[
  {
    "email": "alice@example.com",
    "name": "Alice",
    "class": "5th"
  },
  ...
]

🧪 Deployment & Testing
Deployed via API Gateway (stage: dev)

Lambda permissions managed by IAM role

API is tested using curl and browser for GET requests
curl https://f1tyiyl6k0.execute-api.us-east-1.amazonaws.com/dev/users
[{"email": "sara@example.com", "name": "saraa", "class": "5th"}, {"email": "nadia@example.com", "name": "Nadia", "class": "5th"}]

TODO: add Delete and update API's
