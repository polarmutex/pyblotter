#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/blotter.svg
        :target: https://pypi.python.org/pypi/blotter
.. image:: https://img.shields.io/travis/bryall/blotter.svg
        :target: https://travis-ci.org/bryall/blotter

app to analyze investment blotters


Links:
---------
* `Github <https://github.com/bryall/blotter>`_
"""

from setuptools import setup, find_packages

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Brian Ryall",
    author_email='bryall@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="app to analyze investment blotters",
    entry_points={
        'console_scripts': [
            'blotter=blotter.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='blotter',
    name='blotter',
    packages=find_packages(include=['blotter']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bryall/blotter',
    version='0.1.0',
    zip_safe=False,
)
