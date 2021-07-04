================
autowrapt-logger
================

A Python module logging the elapsed time of methods to ``stdout``. The methods can be specified with ``module:method`` env.
Without modifying your application, you are able to activate this feature.

============
Installation
============
::

    pip install autowrapt-logger

=====
Usage
=====
::

    AUTOWRAPT_BOOTSTRAP=autowrapt_logger INSTRUMENT_LIST="worker:logic_a,worker:logic_b,worker:get_db_data,worker:job" python3 example.py