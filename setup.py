#!/usr/bin/env python

from setuptools import setup

setup(
    name='kvstore',
    version='0.1.0',
    author='Jonatan Enes & Javier Cacheiro',
    author_email='bigdata-dev@listas.cesga.es',
    url='https://github.com/javicacheiro/resource-allocation',
    license='MIT',
    description='Python Resource Allocation API',
    long_description=open('README.rst').read(),
    py_modules=['kvstore'],
    install_requires=['requests'],
    test_suite='tests',
    tests_require=['coverage'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
