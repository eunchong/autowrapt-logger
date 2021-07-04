================
autowrapt-logger
================

A Python module for print logging of a Python application,
without the need to actually modify the Python application itself to
setup the monkey patches.

The package works in conjunction with the ``autowrapt`` and ``wrapt`` module. One would
create post import hook patch modules per ``autowrapt`` module requirements,
and then list the names of the setuptools entrypoints you wish to activate
in the ``AUTOWRAPT_BOOTSTRAP`` environment variable, when executing Python
within the environment that the ``autowrapt`` module is installed.

To understand what is possible, a set of examples is also installed with
this package. To see the examples in action run the following::

    AUTOWRAPT_BOOTSTRAP=autowrapt_logger INSTRUMENT_LIST="worker:logic_a,worker:logic_b,worker:get_db_data,worker:job" python3 example.py

