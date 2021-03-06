#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="django_bend",
    description="Database dump conversion to Django fixtures",
    version="0.0.4",
    license="MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
    keywords='django fixture database dump',
    packages=find_packages(),
    install_requires=[
        'simplejson>=3.8.0',
    ],
)
