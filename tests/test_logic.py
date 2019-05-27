from logic import app, get_page


def test_get_page():
    assert get_page('google') == 'https://google.com'
    assert get_page('not-known') is None


def test_app():
    with app.test_client() as client:
        welcome_page = client.get('/')
        assert welcome_page.status_code == 200
        assert b'inheritance' in welcome_page.data
        assert b'Welcome' in welcome_page.data
