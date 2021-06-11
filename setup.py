import os
import pathlib

import setuptools
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig

SETUP_REQUIRES = ['numpy>=1.20.1']

setuptools.dist.Distribution().fetch_build_eggs(SETUP_REQUIRES)

import subprocess

subprocess.check_call(['./build.sh'])


setup(
    name='kinect2',
    version='0.1.1',
    description='Python Kinect2 Wrapper',
    url='https://github.com/Moskari/pykinect2',
    setup_requires=SETUP_REQUIRES,
    install_requires=SETUP_REQUIRES,
    packages=[''],
    package_dir={'': 'build/src'},
    package_data={'': ['kinect2.py', '_kinect2.so']}
)
