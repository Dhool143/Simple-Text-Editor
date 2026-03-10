# Simple Text Editor Using Stack (Python)

## Overview

This project implements a **simple text editor** that supports three operations:

- Add a character
- Delete the last character
- Undo the last operation

The undo functionality is implemented using a **stack data structure**.

A stack follows the **LIFO (Last In First Out)** principle, meaning the most recent operation is undone first.

---

## Problem Statement

Design a simple text editor that allows:

1. Adding characters
2. Deleting the last character
3. Undoing the last operation

Each operation should update the current text and store the operation in a stack so it can be undone later.

---

## Data Structure Used

### Stack

A stack is used to store the history of operations.

Stack operations used:

| Operation | Description |
|--------|-------------|
| push | Store a new operation |
| pop | Remove the last operation |
| isEmpty | Check if stack is empty |

In Python we use a **list as a stack**:

```python
stack.append()  # push
stack.pop()     # pop