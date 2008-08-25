#!/usr/bin/env python

import urllib

class SqueezePlayer:
    
    def __init__(self, sc, index=None):
        """
        Constructor
        """
        self.sc = sc
        self._cli_keys = ("s_id", "s_uuid", "s_name", "s_ip", "s_model", "b_isplayer", "s_displaytype", "b_canpoweroff", "s_signal_strength", "b_connected")
        self._properties = {}
        self._properties["index"] = index  
        for prop in self._cli_keys:
            type = prop[0]
            value = urllib.unquote(self.sc._request("player %s %i ?" % (prop[2:], index)))
            if type == "i":
                self._properties[prop[2:]] = int(value)
            if type == "s":
                self._properties[prop[2:]] = str(value)
            if type == "b":
                self._properties[prop[2:]] = bool(value)
    
    def __repr__(self):
        return "%s" % (self._properties["id"])
    
    def get_name(self):
        return self._properties["name"]
    
    def get_id(self):
        return self._properties["id"]
 
    def get_uuid(self):
        return self._properties["uuid"]
   
    def get_ip(self):
        return self._properties["ip"]
    
    def show(self, line1="", line2="", duration=3, brightness=4, font="standard", centered=False):
        self.sc._request("%s show line1:%s line2:%s duration:%i brightness:%i font:%s centered:%i" % (self.get_id(), line1, line2, duration, brightness, font, int(centered)))

    def play(self):
        self.sc._request("%s play" % (self.get_id()))

    def stop(self):
        self.sc._request("%s stop" % (self.get_id()))

    def pause(self):
        self.sc._request("%s pause 1" % (self.get_id()))

    def unpause(self):
        self.sc._request("%s pause 0" % (self.get_id()))

    def toggle(self):
        self.sc._request("%s pause" % (self.get_id()))

    def get_mode(self):
        return self.sc._request("%s mode ?" % (self.get_id()))
    
    def get_time(self):
        return self.sc._request("%s time ?" % (self.get_id()))
    
    def seek_to(self, seconds):
        self.sc._request("%s time %s" % (self.get_id(), self.seconds))
        
    def forward(self, seconds):
        self.sc._request("%s time +%s" % (self.get_id(), self.seconds))        

    def rewind(self, seconds):
        self.sc._request("%s time -%s" % (self.get_id(), self.seconds))   

class SqueezeCenterCLI:
    
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
                player = SqueezeCenterPlayer(self, i-1)
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
            