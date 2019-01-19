import pytest
from ..wsgi import app


class TestClass:
    @classmethod
    def setup_class(cls):
        pass

    def test_home_route_get(self):
        """To test / with 200."""
        rv = app.test_client().get('/')
        assert rv.status_code == 200
