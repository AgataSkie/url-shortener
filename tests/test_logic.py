from logic import app, get_page


def test_get_page():
    assert get_page('google') == 'https://google.com'
    assert get_page('not-known') is None


def test_welcome_page():
    with app.test_client() as client:
        welcome_page = client.get('/')
        assert welcome_page.status_code == 200
        assert b'navbar' in welcome_page.data, 'Not inheriting from base.html'
        assert b'Welcome' in welcome_page.data, 'Welcome template not used'


def test_redirection():
    with app.test_client() as client:
        requested_page = client.get('google')
        assert requested_page.status_code == 302
        assert requested_page.location == 'https://google.com'


def test_404():
    with app.test_client() as client:
        requested_page = client.get('nothing')
        assert requested_page.status_code == 404
        assert b'navbar' in requested_page.data, 'Not inheriting from base.html'
        assert b'Page not found' in requested_page.data, '404 template not used'
