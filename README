
Installation
============

Now available on [PyPI](http://pypi.python.org/pypi/pylms) and can be installed using *easy_install*. The package for Debian/Ubuntu is *python-setuptools*. Use your package manager to install this.

Now, type the following. You may need to prefix this with *sudo* if you want a system wide (not a virtualenv) installation.

```easy_install pylms```

Command Line Script
===================

If installed through "easy_install" or via the setup script, there is a new
command called "pylms" that can be used in scripts to control your devices.

```pylms --host 192.168.1.10 --device 00:00:00:00:00:00 play```

For more current help:

```pylms --help```

Documentation
=============

Class documentation, and soon to be usage instructions are now available. [View
Documentation](http://readthedocs.org/docs/pylms-python-logitech-media-server/en/latest).

Features
========

The following functions are supported:

* Retrieval of all configured players
* Retrieval of all properties of configured players
* Retrieval of Volume, Mode, Play Status, Power Status, IR Status, Volume, Bass, Treble, Pitch etc.
* Playlist Control (Play, Add, Insert, Delete, Move etc.)
* Player Control (Play, Stop, Pause, Volume, Muting, Power, IR Remote, Volume, Bass, Treble, Pitch etc.)

[View
Documentation](http://readthedocs.org/docs/pylms-python-logitech-media-server/en/latest/)

Example:


```#!/usr/bin/env python

from pylms.server import Server
from pylms.player import Player

sc = Server(hostname="192.168.1.1", port=9090, username="user", password="password")
sc.connect()

print "Logged in: %s" % sc.logged_in
print "Version: %s" % sc.get_version()

sq = sc.get_player("00:11:22:33:44:55")

print "Name: %s | Mode: %s | Time: %s | Connected: %s | WiFi: %s" % (sq.get_name(), sq.get_mode(), sq.get_time_elapsed(), sq.is_connected, sq.get_wifi_signal_strength())

print sq.get_track_title()
print sq.get_time_remaining()
```
