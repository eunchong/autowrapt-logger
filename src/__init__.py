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
        def hook_module(module_name, methods):
            @wrapt.when_imported(module_name)
            def apply_patches(module):
                try:
                    for method in methods:
                        def wrapping():
                            def logging_wrapper(wrapped, instance, args, kwargs):
                                st = time()
                                result = wrapped(*args, **kwargs)
                                et = time()

                                logging({'name': '%s:%s'%(module_name, method), 'elapsed_time': et-st})
                                return result

                            wrapt.wrap_function_wrapper(module, method, logging_wrapper)
                        wrapping()
                except Exception as e:
                    logging({'error': str(e)})

        for module in modules:
            hook_module(module, modules[module])

    except Exception as e:
        logging({'error': str(e)})

hook()