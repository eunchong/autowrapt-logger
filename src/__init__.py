import os, sys
import json
from time import time
from collections import defaultdict

import wrapt

from .version import __version__

def load(_):
    if not hasattr(sys, "argv"):
        sys.argv = ['']
    return None

def logging(msg):
    print(json.dumps(dict({'autowrapt-logger':__version__}, **msg)))

def logging_wrapper(wrapped, instance, args, kwargs):
    st = time()
    result = wrapped(*args, **kwargs)
    et = time()

    logging({'name': '%s:%s'%(wrapped.__module__, wrapped.__name__), 'elapsed_time': et-st})
    return result

def hook():
    # worker:logic_a,worker:logic_b,worker:get_db_data,worker:job
    INSTRUMENT_LIST = os.environ.get('INSTRUMENT_LIST', None)

    try:
        modules = defaultdict(list)

        # group by module
        for hook in INSTRUMENT_LIST.split(','):
            module, method = hook.split(":")
            modules[module].append(method)
        
        # hook module, when imported
        for module in modules:
            @wrapt.when_imported(module)
            def apply_patches(module):
                try:
                    for method in modules[module.__name__]:
                        wrapt.wrap_function_wrapper(module, method, logging_wrapper)
                except Exception as e:
                    logging({'error': str(e)})

    except Exception as e:
        logging({'error': str(e)})

hook()