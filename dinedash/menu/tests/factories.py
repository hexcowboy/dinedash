"""
This module provides a quick way to generate fake model data
to be used for testing or other data analysis.
"""
from factory import DjangoModelFactory, Faker, SubFactory
from factory.fuzzy import FuzzyChoice

from ..models import Addon, AddonSection, Menu, MenuCategory, MenuItem


class MenuFactory(DjangoModelFactory):
    """Provides fake data for the Menu model"""

    title = Faker("word")
    description = Faker("paragraph")

    class Meta:
        model = Menu


class MenuCategoryFactory(DjangoModelFactory):
    """Provides fake data for the MenuCategory model"""

    title = Faker("word")
    description = Faker("paragraph")
    menu = SubFactory(MenuFactory)

    class Meta:
        model = MenuCategory


class MenuItemFactory(DjangoModelFactory):
    """Provides fake data for the MenuItem model"""

    title = Faker("word")
    description = Faker("paragraph")
    category = SubFactory(MenuCategoryFactory)

    class Meta:
        model = MenuItem


class AddonSectionFactory(DjangoModelFactory):
    """Provides fake data for the MenuItemAddon model"""

    title = Faker("word")
    description = Faker("boolean")
    required = Faker("boolean")
    menu_item = SubFactory(MenuItemFactory)

    class Meta:
        model = AddonSection


class AddonFactory(DjangoModelFactory):
    """Provides fake data for the MenuItemAddon model"""

    description = Faker("word")
    selection = FuzzyChoice(Addon.SELECTION_TYPES, getter=lambda c: c[0])
    section = SubFactory(AddonSectionFactory)

    class Meta:
        model = Addon
