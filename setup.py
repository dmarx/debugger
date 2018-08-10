from setuptools import setup
from os import path
import re

PACKAGE_NAME='debugger'
VERSION = '0.0.1'
README = 'Slightly more sophisticated debugging tool than print()'
HERE = path.abspath(path.dirname(__file__))

#with open(path.join(HERE, 'README.rst'), encoding='utf-8') as fp:
#    README = fp.read()

with open(path.join(HERE, PACKAGE_NAME, '__init__.py'), encoding='utf-8') as fp:
    VERSION = re.search("__version__ = '([^']+)'", fp.read()).group(1)

setup(name=PACKAGE_NAME,
      packages=[PACKAGE_NAME],
      version=VERSION,
      long_description=README,
      description='Slightly more sophisticated debugging tool than print()',
      author='David Marx',
      author_email='david.marx84@gmail.com',
      url='https://gitlab.com/dmarx/debugger',
      license='Simplified BSD License',
      install_requires=['pygments'],
      keywords='debug debugger debugging print bug bugs log logging interactive',
      python_requires='>=3',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Software Development :: Libraries',
          'Topic :: Utilities'
          ]
      )
