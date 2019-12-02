import pytest
from flask_a2 import app, db
from flask_a2.models import User
##### Start the app ######
@pytest.fixture
def app_test():
    app.run(debug=True)
    return app.test_client()


@pytest.fixture
def init_database():
    db.create_all()

    user1 = User(uname='jcnTEST1', pword='pword1', mfa='3476221946')
    user2 = User(uname = 'jcnTEST2', pword='pword2', mfa='3474221046')
    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

    yield db

    db.drop_all()

def test_home_page(app_test):
    response = app_test.get('/')
    assert response.status_code == 200

def test_valid_login_pages_u1(app_test, init_database):
    response = app_test.get('/login', data=dict(uname='jcnTEST1', pword='pword1', mfa='3476221946'), follow_redirects=True)
    assert response.status_code == 200

    response = app_test.get('/account', follow_redirects=True)
    assert response.status_code == 200

    response = app_test.get('/spell_check', follow_redirects=True)
    assert response.status_code == 200

    response = app_test.get('/logout', follow_redirects = True)
    assert response.status_code == 200

def test_valid_login_pages_u2(app_test, init_database):
    response = app_test.get('/login', data=dict(uname='jcnTEST2', pword='pword2', mfa='3474221046'), follow_redirects=True)
    assert response.status_code == 200

    response = app_test.get('/account', follow_redirects=True)
    assert response.status_code == 200

    response = app_test.get('/spell_check', follow_redirects=True)
    assert response.status_code == 200

    response = app_test.get('/logout', follow_redirects = True)
    assert response.status_code == 200

