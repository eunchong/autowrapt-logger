================
autowrapt-logger
================

A Python module logging to ``stdout`` the elapsed time of ``module:method`` specified as an env,
without the need to actually modify the Python application itself to setup the monkey patches.

============
Installation
============
::

    pip install autowrapt-logger

=====
Usage
=====
The autowrapt-logger can then be activated without any code changes required by setting the following environment variable for your Python application::

    AUTOWRAPT_BOOTSTRAP=autowrapt_logger INSTRUMENT_LIST="worker:logic_a,worker:logic_b,worker:get_db_data,worker:job" python3 example.py

This will cause the autowrapt-logger Python package to automatically instrument (like ``module:method``) your Python application. it will print elapsed time for instrumented method.

