import pytest
from flask_a2 import create_app, db
from flask_a2.models import User, History
from flask_a2.routes import flask_app
##### Start the app ######

@pytest.fixture(scope='module')
def app_test(scope='module'):
    app = create_app()
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()


@pytest.fixture(scope='module')
def init_database():
    db.create_all()

    user1 = User(uname='jcnTEST1', pword='pword1', mfa='3476221946')
    user2 = User(uname = 'jcnTEST2', pword='pword2', mfa='3474221046')
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield db

    db.drop_all()


def test_valid_login_pages_u1(app_test):
    response = app_test.post('/login', data=dict(uname='jcnTEST1', mfa='3476221946', pword='pword1'), follow_redirects=True)
    assert response.status_code == 200


    response = app_test.get('/logout', follow_redirects=True)
    assert response.status_code == 200

def test_valid_registration(app_test):
    response = app_test.post('/register', data=dict(uname='julioTEST2', pword='pword2', mfa='13479222965'), follow_redirects=True)
    assert response.status_code == 200

    response = app_test.post('/login', data=dict(uname='julioTEST2', pword='pword2', mfa='13479222965'), follow_redirects=True)
    assert response.status_code == 200


    response = app_test.get('/logout', follow_redirects=True)
    assert response.status_code == 200


