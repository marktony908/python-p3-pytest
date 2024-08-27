# lib/testing/test_not_none.py

from lib.not_none_functions import check_not_none
import pytest

def test_check_not_none_valid():
    assert check_not_none("Test") == "Test"

def test_check_not_none_invalid():
    with pytest.raises(ValueError, match="Value cannot be None"):
        check_not_none(None)
