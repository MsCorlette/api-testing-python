import requests

headers = {
    "x-api-key": "reqres_58dfd40f73c649b0a39c9d15c4f71eae"

}

def test_get_valid_user():
    """Test valid user returns 200 OK"""
    response = requests.get("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 200
    data = response.json()["data"]
    assert data["first_name"] == "Janet"
    assert data["last_name"] == "Weaver"
    print("Positive test passed! Valid user returns 200")

def test_invalid_user():
    """Test that an invalid user returns 404 Not Found"""
    response = requests.get("https://reqres.in/api/users/99", headers=headers)
    assert response.status_code == 404
    print("Negative test 1 passed! Invalid user returns 404")

def test_no_authentication():
    """Test that a no authentication returns 401 for real API(200 Mock API )"""
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    print("Negative test 2 passed! No auth returns 200(mock API behaviour")

def test_invalid_token():
    """Test that an invalid tokens returns 404 or 200 for mock api behaviour """
    fake_headers = {
        "x-api-key": "invalid_fake_token_123"
    }
    response = requests.get("https://reqres.in/api/users/2", headers=fake_headers)
    assert response.status_code == 200
    print("Negative test 3 passed! Invalid token returns 200 (mock API behaviour")

















