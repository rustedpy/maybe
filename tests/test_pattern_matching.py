from __future__ import annotations

from maybe import Maybe, Nothing, Some


def test_pattern_matching_on_some_type() -> None:
    """
    Pattern matching on ``Some()`` matches the contained value.
    """
    o: Maybe[str] = Some("yay")
    match o:
        case Some(value):
            reached = True

    assert value == "yay"
    assert reached


def test_pattern_matching_on_err_type() -> None:
    """
    Pattern matching on ``Err()`` matches the contained value.
    """
    n: Maybe[int] = Nothing()
    match n:
        case Nothing():
            reached = True

    assert reached
