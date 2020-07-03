"""
This module defines tests for Menu models in `menu/models.py`
"""
import pytest
from django.db.utils import IntegrityError

from ..models import MenuCategory, MenuItem
from .factories import (AddonFactory, AddonSectionFactory, MenuCategoryFactory,
                        MenuItemFactory)
from .fixtures import addon, addon_section, menu, menu_category, menu_item

pytestmark = pytest.mark.django_db


class TestMenuModel:
    """Tests for the Menu model"""
    def test_str_representation(self, menu):
        """Test the __str__() function returns the title"""
        assert str(menu) == menu.title


class TestMenuCategoryModel:
    """Tests for the MenuCategory model"""
    def test_str_representation(self, menu_category):
        """Test the __str__() function returns the title"""
        assert str(menu_category) == menu_category.title

    def test_must_belong_to_a_menu(self):
        """Test that a category must belong to a menu object"""
        with pytest.raises(IntegrityError):
            category = MenuCategoryFactory(menu=None)


class TestMenuItemModel:
    """Tests for the MenuItem model"""
    def test_str_representation(self, menu_item):
        """Test the __str__() function returns the title"""
        assert str(menu_item) == menu_item.title

    def test_must_belong_to_a_category(self):
        """Test creating a menu item with a null category fails"""
        with pytest.raises(IntegrityError):
            menu_item = MenuItemFactory(category=None)


class TestAddonSectionModel:
    """Tests for the AddonSection model"""
    def test_str_representation(self, addon_section):
        """Test the __str__() function returns the description"""
        assert str(addon_section) == addon_section.title

    def test_must_belong_to_a_menu_item(self):
        """Test creating a AddonSection fails with a null MenuItem"""
        with pytest.raises(IntegrityError):
            addon_section = AddonSectionFactory(menu_item=None)


class TestAddonModel:
    """Tests for the Addon model"""
    def test_str_representation(self, addon):
        """Test the __str__() function returns the description"""
        assert str(addon) == addon.description

    def test_must_belong_to_a_section(self):
        """Test creating an Addon with a null AddonSection fails"""
        with pytest.raises(IntegrityError):
            addon = AddonFactory(section=None)
