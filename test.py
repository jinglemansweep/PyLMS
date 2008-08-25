#!/usr/bin/env python

from lib.squeezecenter.SqueezeCenter import SqueezeCenter
from lib.squeezecenter.SqueezePlayer import SqueezePlayer

SC_HOST="weasel"
SC_PORT="9090"
SC_USERNAME="admin"
SC_PASSWORD="shredder"

sc = SqueezeCenter(hostname=SC_HOST, port=SC_PORT, username=SC_USERNAME, password=SC_PASSWORD)
sc.connect()

print "Logged in: %s" % sc.logged_in
print "Version: %s" % sc.get_version()

sq = sc.get_player("00:04:20:12:6e:57")

print "Name: %s | Mode: %s | Time: %s | Connected: %s | WiFi: %s" % (sq.name, sq.get_mode(), sq.get_time_elapsed(), sq.is_connected, sq.get_wifi_signal_strength())

print sq.get_track_title()
print sq.get_track_duration()
print sq.get_time_remaining()
print sq.has_permission("power")
print sq.get_pref_value("audiodir")

print sq.set_pref_value("audiodir", "ds0d0")