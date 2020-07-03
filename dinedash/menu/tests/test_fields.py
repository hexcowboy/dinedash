"""
This module defines tests for Menu fields in `menu/fields.py`
"""
import pytest
from django.forms import Form

from ..fields import ShortUUIDField
from .factories import MenuFactory

pytestmark = pytest.mark.django_db


def test_auto_create_uuid():
    """Test that a ShortUUID is generated if none is provided"""
    menu = MenuFactory(uuid=None)
    assert menu.uuid is not None


def test_form_field_auto_returns_none():
    """Test returning data for a form field"""
    uuid = ShortUUIDField().formfield()
    assert uuid is None


def test_form_field_returns_form_field_when_not_auto():
    """Test that a formfield is returned"""
    uuid = ShortUUIDField(auto=False).formfield()
    assert uuid is not None
