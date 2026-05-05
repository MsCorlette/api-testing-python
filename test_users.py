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

def test_create_user():
    """Test that a new user can be created"""
    new_user = {
        "name": "Corlette",
        "job": "QA Analyst"
    }
    response = requests.post(
        "https://reqres.in/api/users",
        json=new_user,
        headers=headers
    )
    assert response.status_code == 201
    assert "id" in response.json()
    assert "createdAt" in response.json()
    print("Positive test passed! New user created with id:", response.json().get("id"))

def test_update_user():
    """Test that an existing user can be updated"""

    updated_user = {
        "name": "Corlette Updated",
        "job": "Senior QA Analyst"

    }

    response = requests.put(
        url="https://reqres.in/api/users/2",
        json=updated_user,
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Corlette Updated"
    assert data["job"] == "Senior QA Analyst"
    assert "updatedAt" in data
    print("PUT test passed! User successfully updated.")

def test_patch_user():
    """Test that a user can be partially updated"""

    patch_data = {
        "job": "Lead QA Analyst"
    }

    response = requests.patch(
        url="https://reqres.in/api/users/2",
        json=patch_data,
        headers=headers
    )

    assert response.status_code == 200

    data = response.json()

    assert data["job"] == "Lead QA Analyst"
    assert "updatedAt" in data
    print("PATCH test passed! User partially updated.")

# Negative Patch test case
def test_patch_user_invalid():
    """Test PATCH on non-existent user"""

    response = requests.patch(
        url="https://reqres.in/api/users/999",
        json={"job": "Test"},
        headers=headers
    )

    # Api behaviour may vary
    assert response.status_code in [200, 404]

def test_delete_user():
    """Test that a user can be deleted"""

    response = requests.delete(
        url="https://reqres.in/api/users/2",
        headers=headers
    )

    assert response.status_code == 204
    assert response.text == ""
    print("DELETE test passed! User successfully deleted.")

# Negative delete test case
def test_delete_user_invalid():
    """Test deleting a non-existing user"""

    response = requests.delete(
        url="https://reqres.in/api/users/999",
        headers=headers
    )

    # API behaviour may vary
    assert response.status_code in [204, 404]

def test_create_and_delete_user():
    """Test creating a user then deleting that same user"""
    new_user = {"name": "Corlette", "job": "QA Analyst"}

    # Step 1 -  Create
    create_response = requests.post(
        url="https://reqres.in/api/users",
        json=new_user,
        headers=headers
    )
    assert create_response.status_code == 201

    # Step 2 - Extract ID
    user_id = create_response.json()["id"]

    # Step 3 Delete same user
    delete_response = requests.delete(
        url=f"https://reqres.in/api/users/{user_id}",
        headers=headers
    )
    assert delete_response.status_code == 204
    print(f"User {user_id} created and deleted successfully!")



























