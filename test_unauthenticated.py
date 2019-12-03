import pytest
from flask_a2 import create_app

##### Testing that the pages exist ######
@pytest.fixture(autouse=True)
def app_test(scope='module'):
    app = create_app()
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


def test_home_page(app_test):
    response = app_test.get("/home")
    assert response.status_code == 200
    
def test_registration_page(app_test):
    response = app_test.get("/register")
    assert response.status_code == 200
    
def test_login_page(app_test):
    response = app_test.get("/login")
    assert response.status_code == 200
    


