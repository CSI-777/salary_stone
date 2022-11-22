#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Nick Maynard",
    author_email='nickmayn@vt.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="The purpose of this project is to host the methods related to the salary stone project. These include a skill extractor from text, a model that allows for prediction of and a variety of other method.",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='salary_stone',
    name='salary_stone',
    packages=find_packages(include=['salary_stone', 'salary_stone.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/nickmayn/salary_stone',
    version='0.2.2',
    zip_safe=False,
)
