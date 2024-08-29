 Overview

The `exercise.py` file provides a `Cache` class for interacting with a Redis database. It includes methods to store and retrieve data in Redis, manage call counts, and track input-output histories using decorators. This module is part of a project focused on understanding basic Redis operations and using Redis as a simple cache in Python.

What `exercise.py` Does

- **Cache Initialization**: Sets up a Redis client and clears existing data.
- **Data Storage**: Stores various data types (strings, bytes, integers, floats) in Redis using randomly generated keys.
- **Data Retrieval**: Retrieves stored data, with support for type conversion back to the original format.
- **Call Counting**: Tracks how many times methods are called using Redis.
- **Input-Output History**: Records the inputs and outputs of function calls in Redis for replay and debugging purposes.
