from string_utils import StringUtils

utils = StringUtils()


# =========================
# capitalize
# =========================

def test_capitalize_positive():
    assert utils.capitalize("hello") == "Hello"


def test_capitalize_number_string():
    assert utils.capitalize("123") == "123"


def test_capitalize_empty_string():
    assert utils.capitalize("") == ""


def test_capitalize_space():
    assert utils.capitalize(" ") == " "


def test_capitalize_none_raises():
    try:
        utils.capitalize(None)
        assert False
    except Exception:
        assert True


# =========================
# trim
# =========================

def test_trim_normal():
    assert utils.trim("  hello  ") == "hello"


def test_trim_no_spaces():
    assert utils.trim("hello") == "hello"


def test_trim_only_spaces():
    assert utils.trim("   ") == ""


def test_trim_empty():
    assert utils.trim("") == ""


def test_trim_none_raises():
    try:
        utils.trim(None)
        assert False
    except Exception:
        assert True


# =========================
# to_list
# =========================

def test_to_list_default():
    assert utils.to_list("a,b,c") == ["a", "b", "c"]


def test_to_list_custom_separator():
    assert utils.to_list("a;b;c", ";") == ["a", "b", "c"]


def test_to_list_single_value():
    assert utils.to_list("abc") == ["abc"]


def test_to_list_empty():
    assert utils.to_list("") == []


def test_to_list_none_raises():
    try:
        utils.to_list(None)
        assert False
    except Exception:
        assert True


# =========================
# contains
# =========================

def test_contains_true():
    assert utils.contains("hello", "ell") is True


def test_contains_false():
    assert utils.contains("hello", "xyz") is False


def test_contains_empty_substring():
    assert utils.contains("hello", "") is True


def test_contains_none_raises():
    try:
        utils.contains(None, "a")
        assert False
    except Exception:
        assert True


# =========================
# delete_symbol
# =========================

def test_delete_symbol_normal():
    assert utils.delete_symbol("hello", "l") == "heo"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("hello", "x") == "hello"


def test_delete_symbol_empty():
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_none_raises():
    try:
        utils.delete_symbol(None, "a")
        assert False
    except Exception:
        assert True
