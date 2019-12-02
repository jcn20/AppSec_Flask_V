import pytest
from flask_a2 import app

##### Testing that the pages exist ######
@pytest.fixture
def app_test():
    app.run(debug=True)
    return app.test_client()

def test_home_page(app_test):
    response = app_test.get("/home")
    assert response.status_code == 200

def test_registration_page(app_test):
    response = app_test.get("/register")
    assert response.status_code == 200

def test_login_page(app_test):
    response = app_test.get("/login")
    assert response.status_code == 200



