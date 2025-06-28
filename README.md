# poltergeist

[![pypi](https://img.shields.io/pypi/v/poltergeist.svg)](https://pypi.python.org/pypi/poltergeist)
[![versions](https://img.shields.io/pypi/pyversions/poltergeist.svg)](https://github.com/alexandermalyga/poltergeist)

[Rust-like error handling](https://doc.rust-lang.org/book/ch09-00-error-handling.html) in Python, with type-safety in mind.

## Features

- 🦀 **Rust-inspired**. Familiar `Result<T, E>` type for Rust developers
- 🔒 **Type-safe**. Full `mypy` compatibility with proper generic typing
- 🎯 **Pattern matching**. Native support for Python 3.10+ match statements
- ⚡ **Async support**. Built-in `catch_async` decorator for async functions
- 🎨 **Clean API**. Minimal, intuitive interface

## Installation

```shell
uv add poltergeist
# or
pip install poltergeist
# or
poetry add poltergeist
```

## Quick Start

Use the `@catch` decorator on any function:

```python
from poltergeist import catch

# Handle an exception type potentially raised within the function
@catch(OSError)
def read_text(path: str) -> str:
    with open(path) as f:
        return f.read()

# Returns an object of type Result[str, OSError]
result = read_text("my_file.txt")
```

Or wrap errors manually:

```python
from poltergeist import Result, Ok, Err

# Equivalent to the decorated function above
def read_text(path: str) -> Result[str, OSError]:
    try:
        with open(path) as f:
            return Ok(f.read())
    except OSError as e:
        return Err(e)
```

Then handle the result in a type-safe way:

```python
# Get the Ok value or re-raise the Err exception
content: str = result.unwrap()

# Get the Ok value or a default if it's an Err
content: str = result.unwrap_or("lorem ipsum")
content: str | None = result.unwrap_or()

# Get the Ok value or compute it from the exception
content: str = result.unwrap_or_else(lambda e: f"The exception was: {e}")

# Get the Err exception or None if it's an Ok
err: OSError | None = result.err()

# Handle the result using structural pattern matching
match result:
    case Ok(content):
        print("Text in upper:", content.upper())
    case Err(e) if isinstance(e, FileNotFoundError):
        print("File not found:", e.filename)
    case Err(e):
        print("Other error:", e)
```

It's also possible to wrap multiple exception types with the decorator:

```python
@catch(OSError, UnicodeDecodeError)
def read_text(path: str) -> str:
    with open(path) as f:
        return f.read()
```

Or manually:

```python
def read_text(path: str) -> Result[str, OSError | UnicodeDecodeError]:
    try:
        with open(path) as f:
            return Ok(f.read())
    except (OSError, UnicodeDecodeError) as e:
        return Err(e)
```

There is also an async-compatible decorator:

```python
from poltergeist import catch_async

@catch_async(OSError)
async def read_text(path: str) -> str:
    with open(path) as f:
        return f.read()

# Returns an object of type Result[str, OSError]
result = await read_text("my_file.txt")
```
