"""Poltergeist - Rust-like error handling in Python, with type-safety in mind."""

from __future__ import annotations

from poltergeist.decorator import catch
from poltergeist.decorator import catch_async
from poltergeist.result import Err
from poltergeist.result import Ok
from poltergeist.result import Result


__all__ = ["Err", "Ok", "Result", "catch", "catch_async"]
