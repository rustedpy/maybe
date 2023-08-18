from __future__ import annotations

import functools
import inspect
import sys
from warnings import warn
from typing import (
    Any,
    Awaitable,
    Callable,
    Final,
    Generic,
    Literal,
    NoReturn,
    Type,
    TypeVar,
    Union,
)

if sys.version_info >= (3, 10):
    from typing import ParamSpec, TypeAlias, TypeGuard
else:
    from typing_extensions import ParamSpec, TypeAlias, TypeGuard


T = TypeVar("T", covariant=True)  # Success type
E = TypeVar("E", covariant=True)  # Error type
U = TypeVar("U")
F = TypeVar("F")
P = ParamSpec("P")
R = TypeVar("R")
TBE = TypeVar("TBE", bound=BaseException)


class Some(Generic[T]):
    """
    A value that indicates success and which stores arbitrary data for the return value.
    """

    __match_args__ = ("some_value",)
    __slots__ = ("_value",)

    def __init__(self, value: T) -> None:
        self._value = value

    def __repr__(self) -> str:
        return "Some({})".format(repr(self._value))

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

    def nothing(self) -> None:
        """
        Return `None`.
        """
        return None

    @property
    def value(self) -> T:
        """
        Return the inner value.

        @deprecated Use `some_value` or `nothing_value` instead. This method will be
        removed in a future version.
        """
        warn(
            "Accessing `.value` on Maybe type is deprecated, please use "
            + "`.some_value` or '.nothing_value' instead",
            DeprecationWarning,
            stacklevel=2,
        )
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

    def expect_nothing(self, message: str) -> NoReturn:
        """
        Raise an UnwrapError since this type is `Some`
        """
        raise UnwrapError(self, message)

    def unwrap(self) -> T:
        """
        Return the value.
        """
        return self._value

    def unwrap_nothing(self) -> NoReturn:
        """
        Raise an UnwrapError since this type is `Some`
        """
        raise UnwrapError(self, "Called `Maybe.unwrap_nothing()` on an `Some` value")

    def unwrap_or(self, _default: U) -> T:
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
        The contained maybe is `Some`, so return `Some` with original value mapped to
        a new value using the passed in function.
        """
        return Some(op(self._value))

    def map_or(self, default: object, op: Callable[[T], U]) -> U:
        """
        The contained maybe is `Some`, so return the original value mapped to a new
        value using the passed in function.
        """
        return op(self._value)

    def map_or_else(self, default_op: object, op: Callable[[T], U]) -> U:
        """
        The contained maybe is `Some`, so return original value mapped to
        a new value using the passed in `op` function.
        """
        return op(self._value)

    def map_nothing(self, op: object) -> Some[T]:
        """
        The contained maybe is `Some`, so return `Some` with the original value
        """
        return self

    def and_then(self, op: Callable[[T], Maybe[U, E]]) -> Maybe[U, E]:
        """
        The contained maybe is `Some`, so return the maybe of `op` with the
        original value passed in
        """
        return op(self._value)

    def or_else(self, op: object) -> Some[T]:
        """
        The contained maybe is `Some`, so return `Some` with the original value
        """
        return self


class Nothing(Generic[E]):
    """
    A value that signifies failure and which stores arbitrary data for the error.
    """

    __match_args__ = ("nothing_value",)
    __slots__ = ("_value",)

    def __init__(self, value: E) -> None:
        self._value = value

    def __repr__(self) -> str:
        return "Nothing({})".format(repr(self._value))

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Nothing) and self._value == other._value

    def __ne__(self, other: Any) -> bool:
        return not (self == other)

    def __hash__(self) -> int:
        return hash((False, self._value))

    def is_some(self) -> Literal[False]:
        return False

    def is_nothing(self) -> Literal[True]:
        return True

    def some(self) -> None:
        """
        Return `None`.
        """
        return None

    def nothing(self) -> E:
        """
        Return the error.
        """
        return self._value

    @property
    def value(self) -> E:
        """
        Return the inner value.

        @deprecated Use `some_value` or `nothing_value` instead. This method will be
        removed in a future version.
        """
        warn(
            "Accessing `.value` on Maybe type is deprecated, please use "
            + "`.some_value` or '.nothing_value' instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._value

    @property
    def nothing_value(self) -> E:
        """
        Return the inner value.
        """
        return self._value

    def expect(self, message: str) -> NoReturn:
        """
        Raises an `UnwrapError`.
        """
        exc = UnwrapError(
            self,
            f"{message}: {self._value!r}",
        )
        if isinstance(self._value, BaseException):
            raise exc from self._value
        raise exc

    def expect_nothing(self, _message: str) -> E:
        """
        Return the inner value
        """
        return self._value

    def unwrap(self) -> NoReturn:
        """
        Raises an `UnwrapError`.
        """
        exc = UnwrapError(
            self,
            f"Called `Maybe.unwrap()` on an `Nothing` value: {self._value!r}",
        )
        if isinstance(self._value, BaseException):
            raise exc from self._value
        raise exc

    def unwrap_nothing(self) -> E:
        """
        Return the inner value
        """
        return self._value

    def unwrap_or(self, default: U) -> U:
        """
        Return `default`.
        """
        return default

    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        """
        The contained maybe is ``Nothing``, so return the maybe of applying
        ``op`` to the error value.
        """
        return op(self._value)

    def unwrap_or_raise(self, e: Type[TBE]) -> NoReturn:
        """
        The contained maybe is ``Nothing``, so raise the exception with the value.
        """
        raise e(self._value)

    def map(self, op: object) -> Nothing[E]:
        """
        Return `Nothing` with the same value
        """
        return self

    def map_or(self, default: U, op: object) -> U:
        """
        Return the default value
        """
        return default

    def map_or_else(self, default_op: Callable[[], U], op: object) -> U:
        """
        Return the maybe of the default operation
        """
        return default_op()

    def map_nothing(self, op: Callable[[E], F]) -> Nothing[F]:
        """
        The contained maybe is `Nothing`, so return `Nothing` with original error mapped to
        a new value using the passed in function.
        """
        return Nothing(op(self._value))

    def and_then(self, op: object) -> Nothing[E]:
        """
        The contained maybe is `Nothing`, so return `Nothing` with the original value
        """
        return self

    def or_else(self, op: Callable[[E], Maybe[T, F]]) -> Maybe[T, F]:
        """
        The contained maybe is `Nothing`, so return the maybe of `op` with the
        original value passed in
        """
        return op(self._value)


# define Maybe as a generic type alias for use
# in type annotations
"""
A simple `Maybe` type inspired by Rust.
Not all methods (https://doc.rust-lang.org/std/option/enum.Option.html)
have been implemented, only the ones that make sense in the Python context.
"""
Maybe: TypeAlias = Union[Some[T], Nothing[E]]

"""
A type to use in `isinstance` checks.
This is purely for convenience sake, as you could also just write `isinstance(res, (Some, Nothing))
"""
SomeNothing: Final = (Some, Nothing)


class UnwrapError(Exception):
    """
    Exception raised from ``.unwrap_<...>`` and ``.expect_<...>`` calls.

    The original ``Maybe`` can be accessed via the ``.maybe`` attribute, but
    this is not intended for regular use, as type information is lost:
    ``UnwrapError`` doesn't know about both ``T`` and ``E``, since it's raised
    from ``Some()`` or ``Nothing()`` which only knows about either ``T`` or ``E``,
    not both.
    """

    _maybe: Maybe[object, object]

    def __init__(self, maybe: Maybe[object, object], message: str) -> None:
        self._maybe = maybe
        super().__init__(message)

    @property
    def maybe(self) -> Maybe[Any, Any]:
        """
        Returns the original maybe.
        """
        return self._maybe


def as_maybe(
    *exceptions: Type[TBE],
) -> Callable[[Callable[P, R]], Callable[P, Maybe[R, TBE]]]:
    """
    Make a decorator to turn a function into one that returns a ``Maybe``.

    Regular return values are turned into ``Some(return_value)``. Raised
    exceptions of the specified exception type(s) are turned into ``Nothing(exc)``.
    """
    if not exceptions or not all(
        inspect.isclass(exception) and issubclass(exception, BaseException)
        for exception in exceptions
    ):
        raise TypeError("as_maybe() requires one or more exception types")

    def decorator(f: Callable[P, R]) -> Callable[P, Maybe[R, TBE]]:
        """
        Decorator to turn a function into one that returns a ``Maybe``.
        """

        @functools.wraps(f)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> Maybe[R, TBE]:
            try:
                return Some(f(*args, **kwargs))
            except exceptions as exc:
                return Nothing(exc)

        return wrapper

    return decorator


def as_async_maybe(
    *exceptions: Type[TBE],
) -> Callable[[Callable[P, Awaitable[R]]], Callable[P, Awaitable[Maybe[R, TBE]]]]:
    """
    Make a decorator to turn an async function into one that returns a ``Maybe``.
    Regular return values are turned into ``Some(return_value)``. Raised
    exceptions of the specified exception type(s) are turned into ``Nothing(exc)``.
    """
    if not exceptions or not all(
        inspect.isclass(exception) and issubclass(exception, BaseException)
        for exception in exceptions
    ):
        raise TypeError("as_maybe() requires one or more exception types")

    def decorator(
        f: Callable[P, Awaitable[R]]
    ) -> Callable[P, Awaitable[Maybe[R, TBE]]]:
        """
        Decorator to turn a function into one that returns a ``Maybe``.
        """

        @functools.wraps(f)
        async def async_wrapper(*args: P.args, **kwargs: P.kwargs) -> Maybe[R, TBE]:
            try:
                return Some(await f(*args, **kwargs))
            except exceptions as exc:
                return Nothing(exc)

        return async_wrapper

    return decorator


def is_some(maybe: Maybe[T, E]) -> TypeGuard[Some[T]]:
    """A typeguard to check if a maybe is an Some

    Usage:
    >>> r: Maybe[int, str] = get_a_maybe()
    >>> if is_some(r):
    >>>     r   # r is of type Some[int]
    >>> elif is_nothing(r):
    >>>     r   # r is of type Nothing[str]
    """
    return maybe.is_some()


def is_nothing(maybe: Maybe[T, E]) -> TypeGuard[Nothing[E]]:
    """A typeguard to check if a maybe is an Nothing

    Usage:
    >>> r: Maybe[int, str] = get_a_maybe()
    >>> if is_some(r):
    >>>     r   # r is of type Some[int]
    >>> elif is_nothing(r):
    >>>     r   # r is of type Nothing[str]
    """
    return maybe.is_nothing()
