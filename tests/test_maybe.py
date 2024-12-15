from __future__ import annotations

import pytest
import result

from maybe import Maybe, Nothing, Some, SomeNothing, UnwrapError, is_nothing, is_some
from maybe.maybe import NOTHING


def test_some_factories() -> None:
    instance = Some(1)
    assert instance._value == 1
    assert instance.is_some() is True


def test_nothing_factory() -> None:
    instance = Nothing()
    assert instance.is_nothing() is True


def test_eq() -> None:
    assert Some(1) == Some(1)
    assert Nothing() == Nothing()
    assert Nothing() == Nothing()
    assert Some(1) != Nothing()
    assert Some(1) != Some(2)
    assert Some(1) == Some(1)
    assert Some(1) != "abc"
    assert Some("0") != Some(0)


def test_const_nothing() -> None:
    assert NOTHING == Nothing()
    assert NOTHING.is_nothing() is True
    assert Some(1) != NOTHING
    assert len({Some(1), NOTHING}) == 2


def test_hash() -> None:
    assert len({Some(1), Nothing(), Some(1), Nothing()}) == 2
    assert len({Some(1), Some(2)}) == 2
    assert len({Some("a"), Nothing()}) == 2


def test_repr() -> None:
    """
    ``repr()`` returns valid code if the wrapped value's ``repr()`` does as well.
    """
    o = Some(123)
    n = Nothing()

    assert repr(o) == "Some(123)"
    assert o == eval(repr(o))  # noqa: S307

    assert repr(n) == "Nothing()"
    assert n == eval(repr(n))  # noqa: S307


def test_some_value() -> None:
    res = Some("haha")
    assert res.some_value == "haha"


def test_some() -> None:
    res = Some("haha")
    assert res.is_some() is True
    assert res.is_nothing() is False
    assert res.some_value == "haha"


def test_some_guard() -> None:
    assert is_some(Some(1))


def test_nothing_guard() -> None:
    assert is_nothing(Nothing())


def test_nothing() -> None:
    res = Nothing()
    assert res.is_some() is False
    assert res.is_nothing() is True


def test_some_method() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.some() == "yay"

    # Unfortunately, it seems the mypy team made a very deliberate and highly contested
    # decision to mark using the return value from a function known to only return None
    # as an error, so we are forced to ignore the check here.
    # See https://github.com/python/mypy/issues/6549
    assert n.some() is None  # type: ignore[func-returns-value]


def test_expect() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.expect("failure") == "yay"
    with pytest.raises(UnwrapError):
        n.expect("failure")


def test_unwrap() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.unwrap() == "yay"
    with pytest.raises(UnwrapError):
        n.unwrap()


def test_unwrap_or() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.unwrap_or("some_default") == "yay"
    assert n.unwrap_or("another_default") == "another_default"


def test_unwrap_or_else() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.unwrap_or_else(str.upper) == "yay"
    assert n.unwrap_or_else(lambda: "default") == "default"


def test_unwrap_or_raise() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.unwrap_or_raise(ValueError) == "yay"
    with pytest.raises(ValueError) as exc_info:  # noqa: PT011
        n.unwrap_or_raise(ValueError)
    assert exc_info.value.args == ()


def test_map() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.map(str.upper).some() == "YAY"
    assert n.map(str.upper).is_nothing()


def test_map_or() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.map_or("hay", str.upper) == "YAY"
    assert n.map_or("hay", str.upper) == "hay"


def test_map_or_else() -> None:
    o = Some("yay")
    n = Nothing()
    assert o.map_or_else(lambda: "hay", str.upper) == "YAY"
    assert n.map_or_else(lambda: "hay", str.upper) == "hay"


def test_and_then() -> None:
    assert Some(2).and_then(sq).and_then(sq).some() == 16
    assert Some(2).and_then(sq).and_then(to_nothing).is_nothing()
    assert Some(2).and_then(to_nothing).and_then(sq).is_nothing()
    assert Nothing().and_then(sq).and_then(sq).is_nothing()

    assert Some(2).and_then(sq_lambda).and_then(sq_lambda).some() == 16
    assert Some(2).and_then(sq_lambda).and_then(to_nothing_lambda).is_nothing()
    assert Some(2).and_then(to_nothing_lambda).and_then(sq_lambda).is_nothing()
    assert Nothing().and_then(sq_lambda).and_then(sq_lambda).is_nothing()


def test_or_else() -> None:
    assert Some(2).or_else(sq).or_else(sq).some() == 2
    assert Some(2).or_else(to_nothing).or_else(sq).some() == 2
    assert Nothing().or_else(lambda: sq(3)).or_else(lambda: to_nothing(2)).some() == 9
    assert (
        Nothing()
        .or_else(lambda: to_nothing(2))
        .or_else(lambda: to_nothing(2))
        .is_nothing()
    )

    assert Some(2).or_else(sq_lambda).or_else(sq).some() == 2
    assert Some(2).or_else(to_nothing_lambda).or_else(sq_lambda).some() == 2


def test_isinstance_result_type() -> None:
    o = Some("yay")
    n = Nothing()
    assert isinstance(o, SomeNothing)
    assert isinstance(n, SomeNothing)
    assert not isinstance(1, SomeNothing)


def test_error_context() -> None:
    n = Nothing()
    with pytest.raises(UnwrapError) as exc_info:
        n.unwrap()
    exc = exc_info.value
    assert exc.maybe is n


def test_slots() -> None:
    """
    Some and Nothing have slots, so assigning arbitrary attributes fails.
    """
    o = Some("yay")
    n = Nothing()
    with pytest.raises(AttributeError):
        o.some_arbitrary_attribute = 1  # type: ignore[attr-defined]
    with pytest.raises(AttributeError):
        n.some_arbitrary_attribute = 1  # type: ignore[attr-defined]


def test_some_ok_or() -> None:
    assert Some(1).ok_or("error") == result.Ok(1)


def test_some_ok_or_else() -> None:
    assert Some(1).ok_or_else(lambda: "error") == result.Ok(1)


def test_nothing_ok_or() -> None:
    assert Nothing().ok_or("error") == result.Err("error")


def test_nothing_ok_or_else() -> None:
    assert Nothing().ok_or_else(lambda: "error") == result.Err("error")


def sq(i: int) -> Maybe[int]:
    return Some(i**2)


def to_nothing(_: int) -> Maybe[int]:
    return Nothing()


def sq_lambda(i: int) -> Maybe[int]:
    return Some(i**2)


def to_nothing_lambda(_: int) -> Maybe[int]:
    return Nothing()
