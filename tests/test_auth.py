def test_login_success(client, user_data):
    # Arrange: register user
    client.post("/api/v1/users/register", json=user_data)

    # Act: login
    response = client.post("/api/v1/users/login", json={
        "email": user_data["email"],
        "password": user_data["password"]
    })

    # Assert
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password(client, user_data):
    client.post("/api/v1/users/register", json=user_data)

    response = client.post("/api/v1/users/login", json={
        "email": user_data["email"],
        "password": "wrongpassword"
    })

    assert response.status_code == 401


def test_login_user_not_found(client):
    response = client.post("/api/v1/users/login", json={
        "email": "doesnotexist@test.com",
        "password": "Password12345"
    })

    assert response.status_code == 401

def test_get_current_user(client, auth_headers):
    response = client.get("/api/v1/users/me", headers=auth_headers)

    assert response.status_code == 200
    assert response.json()["email"] is not None

def test_get_current_user_no_token(client):
    response = client.get("/api/v1/users/me")

    assert response.status_code == 401

def test_get_current_user_invalid_token(client):
    response = client.get("/api/v1/users/me", headers={
        "Authorization": "Bearer invalidtoken"
    })

    assert response.status_code == 401
