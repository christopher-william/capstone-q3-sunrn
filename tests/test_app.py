from typing import Tuple


def test_app_is_created(app):
    assert app.name == 'app'


def test_config_is_loaded(config):
    assert config['DEBUG'] is True


def test_url_not_exits(client):
    assert client.get('/url_not_exits') == 404
