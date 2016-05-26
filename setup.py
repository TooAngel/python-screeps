#!/usr/bin/env python

from distutils.core import setup

from setuptools import find_packages

from screeps._version import __version__


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='screeps',
    version=__version__,
    author='Tobias Wilken',
    author_email='tooangel@tooangel.de',
    maintainer='Tobias Wilken',
    maintainer_email='tooangel@tooangel.de',
    url='https://github.com/TooAngel/python-screeps',
    description='Library connecting to the screeps api.',
    long_description=long_description,
    download_url='https://pypi.python.org/pypi/screeps',
    license='AGPL-3.0',
    platforms=['Any'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',  # noqa
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ],
    packages=find_packages(),
    install_requires=['requests>=2.8.1', 'websocket-client>=0.32.0'],
)
