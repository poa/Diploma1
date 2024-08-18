import pytest
from unittest.mock import patch

from praktikum.burger import Burger
from praktikum.database import Database

from testdata import TData as TD


@pytest.fixture(scope="session")
def test_bun():
    bun = TD.get_test_bun()
    yield bun
    del bun


@pytest.fixture(scope="session")
def test_ingredient():
    ingredient = TD.get_test_ingredient()
    yield ingredient
    del ingredient


@pytest.fixture(scope="session")
def test_db(test_bun, test_ingredient):
    with patch.object(Database, "__init__", lambda self: None):
        db = Database()
        db.buns = [test_bun]
        db.ingredients = [test_ingredient]
        return db


@pytest.fixture(scope="function")
def test_burger(test_bun, test_ingredient):
    burger = Burger()
    burger.set_buns(test_bun)
    burger.add_ingredient(test_ingredient)
    yield burger
    del burger

