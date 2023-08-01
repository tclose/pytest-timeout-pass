"""Demonstration of timeout pass using pytest_timeout.

To use this demo, invoke pytest on it::

   pytest demo.py
"""
import time
import pytest


@pytest.mark.timeout_pass(1)
def test_simple():
    """Basic timeout demonstration, test should pass instead of fail"""
    time.sleep(2)
    assert False
