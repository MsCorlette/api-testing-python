# Api Testing Project - Python & Postman

## This project demonstrates API testing using Python and Postman against the reqres.in demo API. It covers both manual verification in postman and automated test cases in Python, testing positive and negative scenarios including authentication and user validation. 


   
## Tech Stack
 - Python 3.14
 - Request library
 - Postman (manual verification)

## Test Scenarios

| Test | Description | Expected results |
|------|-------------|----------------|
| Valid user | Get existing user | 200 OK |
| Invalid user | Get non-existing user | 404 Not Found |
| No Authentication | Get without API key | 200 (mock API) |
| Invalid token | Get with fake API key | 200 (mock API) |
| Create user | POST new user | 201 Created |
| Update user | PUT full user update | 200 OK |
| Patch user | PATCH partial update | 200 OK | 
| Patch invalid user | PATCH non-existing user | 200 or 404 | 
| Delete user | DELETE existing user | 204 No Content| 
| Delete invalid user | DELETE non-existing user | 204 or 404 | 

## Important Note

reqres.in is a mock/demo API used for practice purposed. It does not enforce strick authentication, meaning some requests with invalid or missing tokens may
still return 200 OK instead of 401 Unauthorised.

In a real-world application, the following would apply: 
- Missing token - 401 Unauthorised
- Invalid token - 401 or 403 Forbidden
- Wrong Credentials - 401 Unauthorised

This project demonstrates understanding of both mock API behaviour and real-world authentication expectations.
## How to Run
1. Clone this repository
2. Install dependencies:
pip install -r requirements.txt
3. Run tests:
python test_users.py

Demo API
https://reqres.in 
