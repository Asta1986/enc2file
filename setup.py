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
      install_requires=['cryptography==2.3.1', 'click==6.7'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points='''
                   [console_scripts]
                   enc2file=enc2file.scripts:cli
                 ''',
      include_package_data=True,
      zip_safe=False)
