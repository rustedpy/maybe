from __future__ import annotations

import sys
from typing import (
    Any,
    Callable,
    Final,
    Generic,
    Literal,
    NoReturn,
    Type,
    TypeVar,
    Union,
)

if sys.version_info >= (3, 10):  # pragma: no cover
    from typing import ParamSpec, TypeAlias, TypeGuard
else:  # pragma: no cover
    from typing_extensions import ParamSpec, TypeAlias, TypeGuard


try:
    import result

    _RESULT_INSTALLED = True
except ImportError:  # pragma: no cover
    _RESULT_INSTALLED = False


T = TypeVar("T", covariant=True)  # Success type
U = TypeVar("U")
E = TypeVar("E")
P = ParamSpec("P")
R = TypeVar("R")
TBE = TypeVar("TBE", bound=BaseException)


class Some(Generic[T]):
    """
    An object that indicates some inner value is present
    """

    __match_args__ = ("some_value",)
    __slots__ = ("_value",)

    def __init__(self, value: T) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"Some({self._value!r})"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Some) and self._value == other._value

    def __ne__(self, other: Any) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash((True, self._value))

    def is_some(self) -> Literal[True]:
        return True

    def is_nothing(self) -> Literal[False]:
        return False

    def some(self) -> T:
        """
        Return the value.
        """
        return self._value

    @property
    def some_value(self) -> T:
        """
        Return the inner value.
        """
        return self._value

    def expect(self, _message: str) -> T:
        """
        Return the value.
        """
        return self._value

    def unwrap(self) -> T:
        """
        Return the value.
        """
        return self._value

    def unwrap_or(self, _default: U) -> T:  # pyright: ignore[reportInvalidTypeVarUse]
        """
        Return the value.
        """
        return self._value

    def unwrap_or_else(self, op: object) -> T:
        """
        Return the value.
        """
        return self._value

    def unwrap_or_raise(self, e: object) -> T:
        """
        Return the value.
        """
        return self._value

    def map(self, op: Callable[[T], U]) -> Some[U]:
        """
        There is a contained value, so return `Some` with original value mapped
        to a new value using the passed in function.
        """
        return Some(op(self._value))

    def map_or(self, _default: object, op: Callable[[T], U]) -> U:
        """
        There is a contained value, so return the original value mapped to a
        new value using the passed in function.
        """
        return op(self._value)

    def map_or_else(self, _default_op: object, op: Callable[[T], U]) -> U:
        """
        There is a contained value, so return original value mapped to a new
        value using the passed in `op` function.
        """
        return op(self._value)

    def and_then(self, op: Callable[[T], Maybe[U]]) -> Maybe[U]:
        """
        There is a contained value, so return the maybe of `op` with the
        original value passed in
        """
        return op(self._value)

    def or_else(self, _op: object) -> Some[T]:
        """
        There is a contained value, so return `Some` with the original value
        """
        return self

    if _RESULT_INSTALLED:

        def ok_or(self, _error: E) -> result.Ok[T]:  # pyright: ignore[reportInvalidTypeVarUse]
            """
            Return a `result.Ok` with the inner value.

            **NOTE**: This method is available only if the `result` package is
            installed.
            """
            return result.Ok(self._value)

        def ok_or_else(self, _op: Callable[[], E]) -> result.Ok[T]:
            """
            Return a `result.Ok` with the inner value.

            **NOTE**: This method is available only if the `result` package is
            installed.
            """
            return result.Ok(self._value)


class Nothing:
    """
    An object that indicates no inner value is present
    """

    __match_args__ = ("nothing_value",)
    __slots__ = ()

    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return "Nothing()"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Nothing)

    def __ne__(self, other: Any) -> bool:
        return not isinstance(other, Nothing)

    def __hash__(self) -> int:
        # A large random number is used here to avoid a hash collision with
        # something else since there is no real inner value for us to hash.
        return hash((False, 982006445019657274590041599673))

    def is_some(self) -> Literal[False]:
        return False

    def is_nothing(self) -> Literal[True]:
        return True

    def some(self) -> None:
        """
        Return `None`.
        """
        return None

    def expect(self, message: str) -> NoReturn:
        """
        Raises an `UnwrapError`.
        """
        exc = UnwrapError(
            self,
            f"{message}",
        )
        raise exc

    def unwrap(self) -> NoReturn:
        """
        Raises an `UnwrapError`.
        """
        exc = UnwrapError(
            self,
            "Called `Maybe.unwrap()` on a `Nothing` value",
        )
        raise exc

    def unwrap_or(self, default: U) -> U:
        """
        Return `default`.
        """
        return default

    def unwrap_or_else(self, op: Callable[[], T]) -> T:
        """
        There is no contained value, so return a new value by calling `op`.
        """
        return op()

    def unwrap_or_raise(self, e: Type[TBE]) -> NoReturn:
        """
        There is no contained value, so raise the exception with the value.
        """
        raise e()

    def map(self, _op: object) -> Nothing:
        """
        Return `Nothing`
        """
        return self

    def map_or(self, default: U, _op: object) -> U:
        """
        Return the default value
        """
        return default

    def map_or_else(self, default_op: Callable[[], U], op: object) -> U:
        """
        Return the result of the `default_op` function
        """
        return default_op()

    def and_then(self, _op: object) -> Nothing:
        """
        There is no contained value, so return `Nothing`
        """
        return self

    def or_else(self, op: Callable[[], Maybe[T]]) -> Maybe[T]:
        """
        There is no contained value, so return the result of `op`
        """
        return op()

    if _RESULT_INSTALLED:

        def ok_or(self, error: E) -> result.Err[E]:
            """
            There is no contained value, so return a `result.Err` with the given
            error value.

            **NOTE**: This method is available only if the `result` package is
            installed.
            """
            return result.Err(error)

        def ok_or_else(self, op: Callable[[], E]) -> result.Err[E]:
            """
            There is no contained value, so return a `result.Err` with the
            result of `op`.

            **NOTE**: This method is available only if the `result` package is
            installed.
            """
            return result.Err(op())

NOTHING = Nothing()

# Define Maybe as a generic type alias for use in type annotations
Maybe: TypeAlias = Union[Some[T], Nothing]
"""
A simple `Maybe` type inspired by Rust.
Not all methods (https://doc.rust-lang.org/std/option/enum.Option.html)
have been implemented, only the ones that make sense in the Python context.
"""

SomeNothing: Final = (Some, Nothing)
"""
A type to use in `isinstance` checks.  This is purely for convenience sake, as you could
also just write `isinstance(res, (Some, Nothing))
"""


class UnwrapError(Exception):
    """
    Exception raised from ``.unwrap_<...>`` and ``.expect_<...>`` calls.

    The original ``Maybe`` can be accessed via the ``.maybe`` attribute, but
    this is not intended for regular use, as type information is lost:
    ``UnwrapError`` doesn't know about ``T``, since it's raised from ``Some()``
    or ``Nothing()`` which only knows about either ``T`` or no-value, not both.
    """

    _maybe: Maybe[object]

    def __init__(self, maybe: Maybe[object], message: str) -> None:
        self._maybe = maybe
        super().__init__(message)

    @property
    def maybe(self) -> Maybe[Any]:
        """
        Returns the original maybe.
        """
        return self._maybe


def is_some(maybe: Maybe[T]) -> TypeGuard[Some[T]]:
    """A typeguard to check if a maybe is a `Some`.

    Usage:

    ```plain
        >>> r: Maybe[int, str] = get_a_maybe()
        >>> if is_some(r):
        ...     r   # r is of type Some[int]
        ... elif is_nothing(r):
        ...     r   # r is of type Nothing[str]
    ```
    """
    return maybe.is_some()


def is_nothing(maybe: Maybe[T]) -> TypeGuard[Nothing]:
    """A typeguard to check if a maybe is a `Nothing`.

    Usage:

    ```plain
        >>> r: Maybe[int, str] = get_a_maybe()
        >>> if is_some(r):
        ...     r   # r is of type Some[int]
        ... elif is_nothing(r):
        ...     r   # r is of type Nothing[str]
    ```
    """
    return maybe.is_nothing()
