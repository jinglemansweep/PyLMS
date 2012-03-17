#!/usr/bin/env python

import os
from distutils.core import setup

setup(
	name="pylms",
	version="0.95",
	description="PyLMS (Python Logitech Media Server API Library)",
	author="JingleManSweep",
	author_email="jinglemansweep@gmail.com",
	url="http://www.louisking.co.uk",
	packages = ["pysqueezecenter"],
    scripts = [os.path.join("bin", "pysqueezecenter"),],
	test_suite = "nose.collector",
    install_requires = [],
	long_description="""Python Wrapper Library for Logitech Media Server CLI (Telnet) Interface""",
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
