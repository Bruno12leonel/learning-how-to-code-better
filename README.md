# learning-how-to-code-better

A hands-on project for practicing the most important best practices in software development.  Each concept is illustrated with a small, working Python example so you can read the code alongside the explanation.

---

## Best practices covered

### 1. Meaningful names
Variables, functions, and modules are named to communicate **intent**.  A reader should be able to understand what a piece of code does without having to trace through its implementation.

```python
# ❌ unclear
def c(a, b):
    return a / b

# ✅ clear
def divide(dividend: float, divisor: float) -> float:
    ...
```

### 2. Single-responsibility functions
Every function does **one thing**.  When a function tries to do too much it becomes hard to test, hard to reuse, and hard to change.

```python
# Each function in calculator/operations.py handles exactly one operation.
def add(first_number: float, second_number: float) -> float: ...
def subtract(first_number: float, second_number: float) -> float: ...
def multiply(first_number: float, second_number: float) -> float: ...
def divide(dividend: float, divisor: float) -> float: ...
```

### 3. Type hints
Type hints make the contract of a function explicit.  They improve IDE auto-complete, catch bugs early with static analysis tools, and act as lightweight documentation.

```python
def multiply(first_number: float, second_number: float) -> float:
    ...
```

### 4. Docstrings
Every public function has a docstring that documents its **purpose**, **parameters**, **return value**, and any **exceptions** it can raise.

```python
def divide(dividend: float, divisor: float) -> float:
    """Return the quotient of two numbers.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        The result of dividing dividend by divisor.

    Raises:
        ValueError: If divisor is zero, since division by zero is undefined.
    """
```

### 5. Explicit error handling
Rather than letting the runtime raise a cryptic `ZeroDivisionError`, the code validates its inputs and raises a descriptive `ValueError` with a helpful message.

```python
if divisor == 0:
    raise ValueError("Cannot divide by zero.")
```

### 6. Automated tests
Every function is covered by unit tests that verify:
- **Normal cases** – expected inputs produce expected outputs.
- **Edge cases** – boundary conditions (zero, negatives, floats) behave correctly.
- **Error cases** – invalid inputs raise the right exceptions with meaningful messages.

---

## Project structure

```
learning-how-to-code-better/
├── calculator/
│   ├── __init__.py        # Package entry-point; re-exports public API
│   └── operations.py      # Arithmetic functions (clean-code example)
├── tests/
│   ├── __init__.py
│   └── test_operations.py # Unit tests for operations.py
└── README.md
```

---

## Running the tests

```bash
python -m unittest discover -s tests
```

All tests should pass with no errors or failures.