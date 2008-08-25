#!/usr/bin/env python

import sys
import telnetlib
import urllib
from SqueezePlayer import SqueezePlayer

class SqueezeCenter:
    
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
            self.logged_in = (result == "")
            
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
            Scan Players
            """
            self.players = []
            player_count = self.get_player_count()
            for i in range(player_count):
                player = SqueezePlayer(self, i-1)
                self.players.append(player)
            return self.players

        def get_player(self, id=None):
            if id:
                for player in self.players:
                    if str(player._properties["id"]).lower() == str(id).lower():
                        return player
                

        def get_version(self):
            self.version = self._request("version ?")
            return self.version
        
        def get_player_count(self):
            self.player_count = self._request("player count ?")
            return int(self.player_count)
        
        def connect(self):
            self._connect()
            self._login()
            

