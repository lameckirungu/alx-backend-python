# ALX Backend Python

A comprehensive collection of advanced Python backend development projects focused on generators, decorators, async operations, testing, and Django middleware.

## Overview

This repository contains coursework from the ALX Backend Python specialization, covering essential topics for building robust backend systems.  Each directory represents a distinct learning module with practical implementations and best practices.

## Projects

### `python-generators-0x00` - Generators & Data Streaming
Master Python generators for memory-efficient data processing.  

**Key Topics:**
- Generator functions with `yield`
- Batch processing and lazy loading
- Streaming data from databases
- Pagination and lazy evaluation
- Aggregate computations on large datasets

**Files:**
- `0-stream_users.py` - Basic user streaming from database
- `1-batch_processing.py` - Process users in configurable batches
- `2-lazy_paginate.py` - Lazy pagination with generators
- `4-stream_ages.py` - Stream and calculate average ages
- `seed. py` - Database connection and setup utilities

### `python-decorators-0x01` - Decorators & Database Operations
Learn decorators for clean, reusable database operation patterns.

**Key Topics:**
- Function decorators and `functools. wraps`
- Database connection management
- Query logging and caching
- Transaction handling and rollback
- Retry logic with exponential backoff

**Files:**
- `0-log_queries.py` - Decorator for logging SQL queries
- `1-with_db_connection.py` - Automatic connection handling
- `2-transactional. py` - Transaction support with rollback
- `3-retry_on_failure.py` - Automatic retry mechanism
- `4-cache_query.py` - Query result caching

### `python-context-async-perations-0x02` - Async Operations & Context Managers
Build asynchronous and context-aware Python applications.

### `0x03-Unittests_and_integration_tests` - Testing Best Practices
Write comprehensive unit and integration tests with mocking.

**Key Topics:**
- Unit testing with `unittest`
- Mocking external dependencies with `unittest.mock`
- Parameterized testing for multiple inputs
- Integration testing patterns
- Fixtures and side effects

**Files:**
- `utils.py` - Helper functions:  `access_nested_map`, `get_json`, `memoize`
- `client.py` - GithubOrgClient implementation
- `test_utils.py` - Unit tests with parameterization
- `test_client.py` - Integration and unit tests
- `fixtures.py` - Test fixtures

### `Django-Middleware-0x03` - Django Middleware Development
Develop custom middleware for Django applications.

### `messaging_app` - Full-Stack Messaging Application
A complete messaging application implementation.  

## 🛠️ Tech Stack

- **Language:** Python 3.7+
- **Databases:** MySQL, SQLite
- **Frameworks:** Django
- **Testing:** `unittest`, `parameterized`
- **Tools:** `functools`, async/await

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager
- MySQL server (for generator projects)

### Setup

```bash
# Clone the repository
git clone https://github.com/lameckirungu/alx-backend-python. git
cd alx-backend-python

# Install dependencies
pip3 install parameterized pycodestyle==2.5 mysql-connector-python
