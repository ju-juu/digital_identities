import pytest
from handler import *


def test_get_user():
    get_user('jesse.hughes@hotmail.com')
    assert True


def test_get_all_users():
    get_all_users()
    assert True
