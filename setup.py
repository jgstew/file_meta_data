"""
py2app/py2exe build script for MyApplication.

Will automatically ensure that all build prerequisites are available
via ez_setup

 Usage (Mac OS X):
     python setup.py py2app

 Usage (Windows):
     python setup.py py2exe
"""
# https://pythonhosted.org/py2app/examples.html#cross-platform
import os
import urllib

# http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
if os.path.isfile("ez_setup.py"):
    urllib.urlretrieve ("http://peak.telecommunity.com/dist/ez_setup.py", "ez_setup.py")
    
import ez_setup
ez_setup.use_setuptools()

import sys
from setuptools import setup

mainscript = 'file_meta_data.py'

if sys.platform == 'darwin':
     extra_options = dict(
         setup_requires=['py2app'],
         app=[mainscript],
         # Cross-platform applications generally expect sys.argv to
         # be used for opening files.
         options=dict(py2app=dict(argv_emulation=True)),
     )
elif sys.platform == 'win32':
     extra_options = dict(
         setup_requires=['py2exe'],
         app=[mainscript],
     )
else:
     extra_options = dict(
         # Normally unix-like platforms will use "setup.py install"
         # and install the main script as such
         scripts=[mainscript],
     )

setup(
    name="file_meta_data",
    **extra_options
)