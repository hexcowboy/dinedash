"""
This module provides fixtures to be used in tests. Fixtures are handled
by pytest.
https://docs.pytest.org/en/latest/fixture.html
"""
import pytest

from .factories import (AddonFactory, AddonSectionFactory, MenuCategory,
                        MenuFactory, MenuItemFactory)


@pytest.fixture
def menu():
    return MenuFactory()


@pytest.fixture
def menu_category():
    return MenuCategory()


@pytest.fixture
def menu_item():
    return MenuItemFactory()


@pytest.fixture
def addon_section():
    return AddonSectionFactory()


@pytest.fixture
def addon():
    return AddonFactory()
