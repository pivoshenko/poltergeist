"""Module that contains decorators for error handling."""

from __future__ import annotations

import functools

from typing import TYPE_CHECKING
from typing import ParamSpec
from typing import TypeVar

from poltergeist.result import Err
from poltergeist.result import Ok
from poltergeist.result import Result


if TYPE_CHECKING:
    from collections.abc import Awaitable
    from collections.abc import Callable


_T = TypeVar("_T")
_E = TypeVar("_E", bound=BaseException)
_P = ParamSpec("_P")


def catch(
    *errors: type[_E],
) -> Callable[[Callable[_P, _T]], Callable[_P, Result[_T, _E]]]:
    """Catch specified exceptions and return ``Ok`` on success or ``Err`` on exception."""

    def decorator(func: Callable[_P, _T]) -> Callable[_P, Result[_T, _E]]:
        @functools.wraps(func)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> Result[_T, _E]:
            try:
                result = func(*args, **kwargs)
            except errors as e:
                return Err(e)
            return Ok(result)

        return wrapper

    return decorator


def catch_async(
    *errors: type[_E],
) -> Callable[[Callable[_P, Awaitable[_T]]], Callable[_P, Awaitable[Result[_T, _E]]]]:
    """Catch specified exceptions in async functions.

    Return ``Ok`` on success or ``Err`` on exception.
    """

    def decorator(func: Callable[_P, Awaitable[_T]]) -> Callable[_P, Awaitable[Result[_T, _E]]]:
        @functools.wraps(func)
        async def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> Result[_T, _E]:
            try:
                result = await func(*args, **kwargs)
            except errors as e:
                return Err(e)
            return Ok(result)

        return wrapper

    return decorator
