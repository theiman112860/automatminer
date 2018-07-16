#!/usr/bin/env python

from setuptools import setup, find_packages
import os
import multiprocessing, logging

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='matbench',
        version='0.1.0',
        description='benchmarking of machine learning models in material science',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        url='https://github.com/hackingmaterials/matbench',
        author=['Alireza Faghaninia', 'Alex Dunn', 'Qi Wang', 'Anubhav Jain'],
        author_email=['alireza.faghaninia@gmail.com', 'denhaus@gmail.com', 'qwang3@lbl.gov', 'ajain@lbl.gov'],
        license='modified BSD',
        packages=find_packages(),
        package_data={},
        zip_safe=False,
        install_requires=[],
        extras_require={},
        classifiers=['Programming Language :: Python :: 3.6',
                     'Development Status :: 4 - Beta',
                     'Intended Audience :: Science/Research',
                     'Intended Audience :: System Administrators',
                     'Intended Audience :: Information Technology',
                     'Operating System :: OS Independent',
                     'Topic :: Other/Nonlisted Topic',
                     'Topic :: Scientific/Engineering'],
        test_suite='nose.collector',
        tests_require=['nose'],
        scripts=[]
    )