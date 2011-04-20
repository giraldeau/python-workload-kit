from distutils.core import setup
import os
import sys

setup(
    name = "python-workload-kit",
    version = "0.0.1",
    url = 'http://www.lttng.org/',
    author = 'Francis Giraldeau',
    author_email = 'francis.giraldeau@gmail.com',
    description = 'Utilities to generate synthetic system workloads',
    package_dir = {'': 'src'},
    packages = ['wk', 'wk.rpc'],
    scripts = ['bin/wk']
)
