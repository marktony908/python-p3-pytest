# lib/testing/test_string.py

from lib.string_functions import return_string, interpolate_string

def test_return_string():
    assert return_string() == "Hello, World!"

def test_interpolate_string():
    assert interpolate_string("Alice") == "Welcome, Alice!"
