# Claude Workshop — Session 1

A simple Python calculator module built during a Claude Code workshop.

## Functions

| Function | Description |
|----------|-------------|
| `add(a, b)` | Returns `a + b` |
| `subtract(a, b)` | Returns `a - b` |
| `multiply(a, b)` | Returns `a * b` |
| `divide(a, b)` | Returns `a / b`, raises `ValueError` on division by zero |
| `power(a, b)` | Returns `a ** b` |

## Usage

```python
from calculator import add, subtract, multiply, divide, power

add(10, 3)       # 13
subtract(10, 3)  # 7
multiply(10, 3)  # 30
divide(10, 3)    # 3.3333...
power(10, 3)     # 1000
```

## Running the demo

```bash
python calculator.py
```

## Running the tests

```bash
pip install pytest
pytest test_calculator.py -v
```
