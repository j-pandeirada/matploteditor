#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='matploteditor',
    version='0.0.1',
    description="The figure editor all matplotlib users deserve.",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Joao Pandeirada",
    author_email='jdpandeirada@gmail.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    license="BSD license",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
    install_requires=[
        'numpy',
        'matplotlib',
        'pyqt5',
    ],
)
