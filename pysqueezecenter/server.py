#!/usr/bin/env python

"""
PySqueezeCenter: Python Wrapper for Logitech SqueezeCenter CLI (Telnet) Interface
Copyright (C) 2008 JingleManSweep <jinglemansweep [at] gmail [dot] com>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

import sys
import telnetlib
import urllib
from player import Player

class Server:
    
        def __init__(self, hostname="localhost", port=9090, username="", password=""):
            """
            Constructor
            """
            self.debug = False
            self.hostname = hostname
            self.port = port
            self.username = username
            self.password = password
            self.version = ""
            self.player_count = 0
            self.players = []
            
        def _connect(self):
            """
            Connect
            """
            self.tn = telnetlib.Telnet(self.hostname, self.port)
        
        def _login(self):
            """
            Login
            """
            result = self._request("login %s %s" % (self.username, self.password))
            self.logged_in = (result == "******")
            
        def _request(self, command_string):
            """
            Request
            """
            self.tn.write(command_string + "\n")
            response = urllib.unquote(self.tn.read_until("\n"))
            result = response[len(command_string)-1:-1]
            return result

        def get_players(self):
            """
            Get Players
            """
            self.players = []
            player_count = self.get_player_count()
            for i in range(player_count):
                player = Player(self, i-1)
                self.players.append(player)
            return self.players

        def get_player(self, id=None):
            """
            Get Player
            """
            if id:
                for player in self.players:
                    if str(player.id) == str(id).lower():
                        return player

        def get_version(self):
            """
            Get Version
            """
            self.version = self._request("version ?")
            return self.version
        
        def get_player_count(self):
            """
            Get Number Of Players
            """
            self.player_count = self._request("player count ?")
            return int(self.player_count)
        
        def connect(self):
            """
            Connect
            """
            self._connect()
            self._login()
            self.get_players()
            

