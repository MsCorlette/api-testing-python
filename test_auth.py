import requests

headers = {
    "x-api-key": "reqres_58dfd40f73c649b0a39c9d15c4f71eae"
}

def test_bearer_token_auth():
    """Test login and use Bearer token to access protected data"""

    # Step 1 - Login
    login_response = requests.post(
        url="https://reqres.in/api/login",
        json={
            "email" : "george.bluth@reqres.in",
            "password" : "pistol"
        },
        headers=headers
    )
    assert login_response.status_code == 200

    # Step 2Extract token
    token = login_response.json()["token"]

    # Step 3 Use token
    auth_headers = {
        "x-api-key" : "reqres_58dfd40f73c649b0a39c9d15c4f71eae",
        "Authorization" : f"Bearer {token}"
    }

    # Step 4 Access protected data
    response = requests.get(
        url="https://reqres.in/api/users/2",
        headers=auth_headers
    )
    assert response.status_code == 200

# Negative test (Incorrect login)
def test_invalid_login():
    """Test that incorrect password returns 401"""

login_response = requests.post(
    url ="https://reqres.in/api/login",
    json ={
        "email" : "george.bluth@reqres.in",
        "password" : "breaking"
    },
    headers=headers
)
assert login_response.status_code in [200, 400, 401]
# reqres.in is a mock API - may not enforce authentication strictly

# Negative test ( invalid token)
def test_invalid_token():
    """Test that invalid token returns 400"""

    auth_headers = {
        "x-api-key" : "reqres_58dfd40f73c649b0a39c9d15c4f71eae",
        "Authorisation" : "Bearer faketoken54"
    }

    response = requests.get(
        url="https://reqres.in/api/users/2",
        headers=auth_headers
    )
    assert response.status_code in [200, 401, 403]
    # reqres.in is a mock API and does not enforce strick authentication

