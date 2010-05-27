#!/usr/bin/env python

import os

from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(
	name="pysqueezecenter",
	version="0.9",
	description="PySqueezeCenter",
	author="Louis King",
	author_email="jinglemansweep@gmail.com",
	url="http://www.louisking.co.uk",
	packages = find_packages(),
        scripts = [os.path.join("bin", "pysqueezecenter"),],
	test_suite = "nose.collector",
        install_requires = [],
	long_description="""Python Wrapper Library for Logitech SqueezeCenter CLI (Telnet) Interface""",
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Environment :: Console",
		"Intended Audience :: Developers",
	        "Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Natural Language :: English",
		"Operating System :: POSIX :: Linux",
		"Programming Language :: Python :: 2.5",
	]
)
