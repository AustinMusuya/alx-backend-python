# Python Utilities Testing Project

This project contains utility functions and their corresponding unit tests, written in Python 3.7 and compliant with Ubuntu 18.04 standards.

## 📁 Project Structure

```
.
├── utils.py              # Utility module with reusable functions
├── test_utils.py         # Unit tests using unittest and parameterized
├── README.md             # Project documentation
```

## 🛠️ Requirements

- Python 3.7
- `parameterized` module for test expansion
- `pycodestyle` version 2.5
- Unix-based system (Ubuntu 18.04 LTS recommended)

Install dependencies:

```bash
pip install parameterized pycodestyle==2.5
```

## 📌 Features

- `access_nested_map`: Retrieve a value from a nested dictionary using a sequence of keys.
- Full unit test coverage using `unittest` and `parameterized`.
- PEP8-compliant (`pycodestyle` 2.5).
- All modules, classes, and functions are type-annotated and documented with complete sentences.

## ✅ Running Tests

You can run all tests using the built-in `unittest` module:

```bash
python3 -m unittest test_utils.py
```

## 🧪 Sample Test Cases

The test suite includes:

- Valid nested dictionary access
- Path sequences of varying depth
- Parameterized inputs for streamlined coverage

## ⚙️ Conventions Followed

- All files begin with a proper shebang (`#!/usr/bin/env python3`)
- All files end with a newline
- All modules, classes, and functions include clear, complete-sentence docstrings
- Executable permissions (`chmod +x`) are applied to scripts
- Type hints are used throughout the codebase

## 📄 License

This project is licensed for educational and internal development use.

## 👤 Author

Maintained by [Your Name Here]. Contributions welcome via pull request or fork.
