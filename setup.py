# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name='enc2file',
    version='0.1',
    description='Module to easily encrypt and decrypt strings using cryptography\'s Fernet recipe.',
    url='https://github.com/Asta1986/enc2file',
    author='Asta1986',
    author_email='psljp@protonmail.com',
    license='GPL-3',
    packages=find_packages(),
    install_requires=['cryptography>=2.1.4'],
    test_suite='nose.collector',
    tests_require=['nose>=1.3.7'],
    include_package_data=True,
    zip_safe=False)
