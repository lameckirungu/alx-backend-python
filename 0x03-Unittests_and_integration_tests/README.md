# Unittests and Integration Tests

* Project: Unittests and Integration Tests
* Directory: `0x03-Unittests_and_integration_tests`
* Repo: `alx-backend-python`

Overview
--------
This project contains unit and integration tests for small helper modules used in the ALX backend Python projects. The exercise focuses on:
- Writing unit tests that cover normal and edge cases.
- Using parameterization to test many inputs.
- Mocking external dependencies (HTTP calls, properties, etc.) with unittest.mock.
- Writing integration tests that only mock external I/O while exercising internal code paths.
- Applying testing patterns: mocking, parameterization, fixtures, memoization.

Learning goals
--------------
- Use `unittest`, `unittest.mock` and `parameterized` to write tests.
- Mock functions and properties
- Write integration tests using fixtures and side effects.
- Keep code style and documentation to project requirements.

Repository layout
-----------------
- `utils.py` - helper functions: `access_nested_map`, `get_json`, `memoize`
- `client.py` - GithubOrgClient implementation used by tests
- `fixtures.py` - fixtures for integration tests
- `test_utils.py` - unit tests for `utils.py`
- `test_client.py` - unit + integration test for `client.py`

Requirements
------------
- OS: Ubuntu 18.04 LTS (grading environmetn)
- Python 3.7
- All files must:
    - Start with the exact shebang: `#!/usr/bin/env python3`
    - Be executable
    - End with a new line
    - Contain module, class and function docstrings
    - Use type annotations for functions / coroutines
    - Follow pycodestyle (v2.5) rules

Install dependencies
--------------------
Install test helper libraries locally:
```python
pip3 install parameterized
pip3 install pycodestyle==2.5
```

Running tests
-------------
Run a single test file:
```python
python3 -m unittest 0x03-Unittest_and_integration_tests/test_utils.py
```
Run a single test case / method:
```python
python3 -m unittest 0x03-Unittests_and_integration_tests.test_utils.TestAccessNestedMap.test_access_nested_map
```
Run all tests (discovery):
```python
python3 -m unittest discover -v
```

Notes about tests
-----------------
- Unit tests must mock external calls (`requests.get`, network, DB, etc.). Use `unittest.mock.patch` or `patch.object`.
- Parameterize tests using `parameterized.expand` and `parameterized_class` for fixtures-based integration tests.
- For memoize tests, mock the underlyingi method and ensure it is called only once.
- Integration tests in `test_client.py` use `fixtures.py` and `patch requests.get` with side_effect to return appropriate JSON payloads.

Style checks
------------
```python
pycodestyle --max-line-length=79
```

Scoring / Tasks summary
-----------------------
<p>This project contains 9 tasks that exercise parameterization, mocking and integration testing: </p>

0. Parameterize access_nested_map success cases (test_utils.py)
1. Parameterize access_nested_map exceptions (test_utils.py)
2. Mock HTTP calls for get_json (test_utils.py)
3. Test memoize decorator (test_utils.py)
4. Test GithubOrgClient.org with patch + parameterized (test_client.py)
5. Test `_public_repos_url` by mocking org property (test_client.py)
6. Test public_repos by patching `get_json` and `_public_repos_url` (test_client.py)
7. Test `has_license` with parameterized inputs (test_client.py)
8. Integration tests for `public_repos` suign fixtures and `requests.get.side_effect (test_client.py)

Author
------
- [Lameck Irungu](https://github.com/lameckirungu)

License
-------
This project is licensed under the [MIT License](LICENSE), unless otherwise specified.