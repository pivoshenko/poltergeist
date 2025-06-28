"""Module that contains Rust-like result types."""

from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Any
from typing import Generic
from typing import NoReturn
from typing import TypeVar
from typing import final
from typing import overload


if TYPE_CHECKING:
    from collections.abc import Callable


_T_co = TypeVar("_T_co", covariant=True)
_E_co = TypeVar("_E_co", bound=BaseException, covariant=True)
_D = TypeVar("_D")


@final
class Ok(Generic[_T_co]):
    """Represents a successful result containing a value."""

    __slots__ = ("_value",)
    __match_args__ = ("_value",)

    def __init__(self, value: _T_co) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"Ok({self._value!r})"

    def __eq__(self, __o: object, /) -> bool:
        return isinstance(__o, Ok) and self._value == __o._value

    def __hash__(self) -> int:
        return hash(("Ok", self._value))

    def err(self) -> None:
        """Return None since this is not an error."""

    def unwrap(self) -> _T_co:
        """Return the wrapped value."""
        return self._value

    @overload
    def unwrap_or(self) -> _T_co: ...

    @overload
    def unwrap_or(self, default: _D) -> _T_co: ...

    def unwrap_or(self, default: _D | None = None) -> _T_co | _D:  # noqa: ARG002
        """Return the wrapped value, ignoring the default."""
        return self.unwrap()

    def unwrap_or_else(self, op: Callable[[_E_co], _D]) -> _T_co:  # noqa: ARG002
        """Return the wrapped value, ignoring the operation."""
        return self.unwrap()


@final
class Err(Generic[_E_co]):
    """Represents an error result containing an exception."""

    __slots__ = ("_value",)
    __match_args__ = ("_value",)

    def __init__(self, value: _E_co) -> None:
        self._value = value

    def __repr__(self) -> str:
        return f"Err({self._value!r})"

    def __eq__(self, __o: object, /) -> bool:
        return (
            isinstance(__o, Err)
            and type(__o._value) is type(self._value)
            and __o._value.args == self._value.args
        )

    def __hash__(self) -> int:
        return hash(("Err", type(self._value), self._value.args))

    def err(self) -> _E_co:
        """Return the wrapped exception."""
        return self._value

    def unwrap(self) -> NoReturn:
        """Raise the wrapped exception."""
        raise self._value

    @overload
    def unwrap_or(self) -> None: ...

    @overload
    def unwrap_or(self, default: _D) -> _D: ...

    def unwrap_or(self, default: Any = None) -> Any:
        """Return the default value instead of the error."""
        return default

    def unwrap_or_else(self, op: Callable[[_E_co], _D]) -> _D:
        """Apply the operation to the error and return the result."""
        return op(self._value)


Result = Ok[_T_co] | Err[_E_co]
