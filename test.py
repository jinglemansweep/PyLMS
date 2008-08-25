#!/usr/bin/env python

from lib.squeezecenter.SqueezeCenter import SqueezeCenter
from lib.squeezecenter.SqueezePlayer import SqueezePlayer

SC_HOST="weasel"
SC_PORT="9090"
SC_USERNAME="admin"
SC_PASSWORD="shredder"

sc = SqueezeCenter(hostname=SC_HOST, port=SC_PORT, username=SC_USERNAME, password=SC_PASSWORD)
sc.connect()
print sc.logged_in
print "Version: %s!" % sc.get_version()
players = sc.get_players()
print players
sq = sc.get_player("00:04:20:12:6e:57")
print sq.get_name()
sq.show(line1="HELLO", line2="TPOO")
print sq.get_mode()
print sq.get_time()