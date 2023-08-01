===================
pytest-timeout-pass
===================

|python| |version| |anaconda| |ci| |pre-commit|

.. |version| image:: https://img.shields.io/pypi/v/pytest-timeout-pass.svg
  :target: https://pypi.python.org/pypi/pytest-timeout-pass

.. |ci| image:: https://github.com/pytest-dev/pytest-timeout-pass/workflows/build/badge.svg
  :target: https://github.com/pytest-dev/pytest-timeout-pass/actions

.. |python| image:: https://img.shields.io/pypi/pyversions/pytest-timeout-pass.svg
  :target: https://pypi.python.org/pypi/pytest-timeout-pass/

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/pytest-dev/pytest-timeout-pass/master.svg
   :target: https://results.pre-commit.ci/latest/github/pytest-dev/pytest-timeout-pass/master


This plugin will time long-running tests, kill them when it has passed the initialisation phase
and mark them as passed (i.e. assuming internal validation has completed successfully
in the process to be tested). It is based on the `pytest-timeout <https://github.com/pytest-dev/pytest-timeout>`__ plugin .


Usage
=====

Install with pip e.g.::

   pip install pytest-timeout-pass

.. code:: python

   @pytest.mark.timeout_pass(60)
   def test_foo():
       pass

By default the plugin will not time out any tests, you must specify a
valid timeout for the plugin to interrupt long-running tests.  A
timeout is always specified as a number of seconds, and can be
defined in a number of ways, from low to high priority:

1. You can set a global timeout in the `pytest configuration file`__
   using the ``timeout`` option.  E.g.:

   .. code:: ini

      [pytest]
      timeout_pass = 300

2. The ``PYTEST_TIMEOUT_PASS`` environment variable sets a global timeout
   overriding a possible value in the configuration file.

3. The ``--timeout`` command line option sets a global timeout
   overriding both the environment variable and configuration option.

4. Using the ``timeout`` marker_ on test items you can specify
   timeouts on a per-item basis:

   .. code:: python

      @pytest.mark.timeout_pass(300)
      def test_foo():
          pass

Setting a timeout to 0 seconds disables the timeout, so if you have a
global timeout set you can still disable the timeout by using the
mark.


The ``timeout`` Marker API
==========================

The full signature of the timeout marker is:

.. code:: python

   pytest.mark.timeout_pass(timeout=0)

See the marker api documentation_ and examples_ for the various ways
markers can be applied to test items.

.. _documentation: https://docs.pytest.org/en/latest/mark.html

.. _examples: https://docs.pytest.org/en/latest/example/markers.html#marking-whole-classes-or-modules

