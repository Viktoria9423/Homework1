import pytest
from string_utils import StringUtils

utils = StringUtils()


# capitalize

def test_capitalize_positive():
    assert utils.capitalize("hello") == "Hello"


def test_capitalize_already_capitalized():
    assert utils.capitalize("Hello") == "Hello"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_space():
    assert utils.capitalize(" ") == " "


def test_capitalize_none():
    assert utils.capitalize(None) is None


# trim

def test_trim_positive():
    assert utils.trim("  hello  ") == "hello"


def test_trim_no_spaces():
    assert utils.trim("hello") == "hello"


def test_trim_only_spaces():
    assert utils.trim("   ") == ""


def test_trim_empty():
    assert utils.trim("") == ""


def test_trim_none():
    with pytest.raises(AttributeError):
        utils.trim(None)


# to_list

def test_to_list_default_delimiter():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]


def test_to_list_custom_delimiter():
    assert utils.to_list("a;b;c", ";") == ["a", "b", "c"]


def test_to_list_no_delimiter():
    assert utils.to_list("abc") == ["abc"]


def test_to_list_empty_string():
    assert utils.to_list("") == []


def test_to_list_none():
    assert utils.to_list(None) is None


# contains

def test_contains_positive():
    assert utils.contains("hello", "ell") is True


def test_contains_negative():
    assert utils.contains("hello", "xyz") is False


def test_contains_empty_substring():
    assert utils.contains("hello", "") is True


def test_contains_none():
    assert utils.contains(None, "a") is False


# delete_symbol

def test_delete_symbol_positive():
    assert utils.delete_symbol("hello", "l") == "heo"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("hello", "x") == "hello"


def test_delete_symbol_empty_string():
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_none():
    assert utils.delete_symbol(None, "a") is None
