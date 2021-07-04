import imp
from os import path

from setuptools import setup

VERSION = imp.load_source('version', path.join('.', 'src', 'version.py'))
VERSION = VERSION.__version__

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup_kwargs = dict(
    name = 'autowrapt-logger',
    version = VERSION,
    description = 'logging by environment',
    long_description_content_type='text/x-rst',
    long_description=read('README.rst'),
    author = 'eunchong',
    license = 'BSD',
    url = 'https://github.com/eunchong/autowrapt-logger',
    packages = ['autowrapt_logger'],
    package_dir = {'autowrapt_logger': 'src'},
    install_requires=['autowrapt>=1.0'],
    entry_points={
                'autowrapt_logger':  ['string=autowrapt_logger:load'],
    }
)

setup(**setup_kwargs)
