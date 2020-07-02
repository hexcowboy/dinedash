"""
This module defines tests for Menu urls
"""
import pytest
import shortuuid

from .factories import MenuFactory

pytestmark = pytest.mark.django_db


@pytest.mark.urls('config.urls')
class TestMenuURLs:
    """Tests for the Menu urls"""

    def test_list_view_resolves(self, client):
        """Test /menus/"""
        response = client.get('/menus/')
        assert response.status_code == 200

    def test_detail_view_doesnt_resolve_without_uuid(self, client):
        """Test that a valid ShortUUID must be supplied for detail view"""
        response = client.get('/menus/abcd')
        assert response.status_code == 404

    def test_detail_view_resolves_valid_uuid(self, client):
        """Test that supplying the ShortUUID of a real model works"""
        uuid = shortuuid.uuid()
        menu = MenuFactory(uuid=uuid)
        response = client.get(f'/menus/{uuid}')
        assert response.status_code == 200
        assert str.encode(menu.title) in response.content
