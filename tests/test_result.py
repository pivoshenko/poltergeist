import pytest

from poltergeist import Err, Ok


def test_ok() -> None:
    result = Ok("abc")

    match result:
        case Ok(v):
            assert v == "abc"
        case _:
            pytest.fail("Should have been Ok")

    assert result.err() is None

    assert result.unwrap() == "abc"

    assert result.unwrap_or() == "abc"

    assert result.unwrap_or("aaa") == "abc"

    assert result.unwrap_or_else(lambda e: str(e)) == "abc"


def test_ok_eq() -> None:
    result = Ok("abc")
    assert result == Ok("abc")
    assert result != Ok("aaa")
    assert result != Err(Exception("abc"))
    assert result != "abc"


def test_ok_repr() -> None:
    result = Ok("abc")
    assert repr(result) == "Ok('abc')"


def test_error() -> None:
    result = Err(ValueError("abc"))

    match result:
        case Err(e):
            assert type(e) == ValueError
            assert e.args == ("abc",)
        case _:
            pytest.fail("Should have been Err")

    assert type(result.err()) == ValueError
    assert result.err().args == ("abc",)

    with pytest.raises(ValueError) as excinfo:
        result.unwrap()

    assert type(excinfo.value) == ValueError
    assert excinfo.value.args == ("abc",)

    assert result.unwrap_or() is None

    assert result.unwrap_or("aaa") == "aaa"

    assert result.unwrap_or_else(lambda e: f"Exception is {e}") == "Exception is abc"


def test_err_eq() -> None:
    result = Err(ValueError("abc"))
    assert result == Err(ValueError("abc"))
    assert result != Err(ValueError("aaa"))
    assert result != Err(ValueError("abc", 1))
    assert result != Err(Exception("abc"))
    assert result != Ok("abc")
    assert result != "abc"


def test_err_repr() -> None:
    result = Err(ValueError("Incorrect value!"))
    assert repr(result) == "Err(ValueError('Incorrect value!'))"
