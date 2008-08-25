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

import urllib

class SqueezePlayer:
    
    def __init__(self, sc, index=None):
        """
        Constructor
        """
        self.sc = sc
        self.index = None
        self.id = None
        self.uuid = None
        self.name = None
        self.model = None
        self.ip_address = None
        self.is_connected = None
        self.is_player = None
        self.display_type = None
        self.can_power_off = None
        self.wifi_signal_strength = None
        self.mode = None
        self.time = None
        self.power_state = None
        self.volume = None
        self.mixing = None
        self._update(index)

    def __repr__(self):
        return self.id
    
    def _request(self, command_string):
        return self.sc._request("%s %s" % (self.id, command_string))
    
    def _update(self, index):
        self.index = index
        self.id = str(urllib.unquote(self.sc._request("player id %i ?" % index)))
        self.uuid = str(urllib.unquote(self.sc._request("player uuid %i ?" % index)))
        self.name = str(urllib.unquote(self.sc._request("player name %i ?" % index)))    
        self.ip_address = str(urllib.unquote(self.sc._request("player ip %i ?" % index)))    
        self.model = str(urllib.unquote(self.sc._request("player model %i ?" % index)))   
        self.display_type = str(urllib.unquote(self.sc._request("player displaytype %i ?" % index)))
        self.wifi_signal_strength = str(urllib.unquote(self.sc._request("player signal_strength %i ?" % index)))
        self.can_power_off = bool(urllib.unquote(self.sc._request("player canpoweroff %i ?" % index))) 
        self.is_player = bool(urllib.unquote(self.sc._request("player isplayer %i ?" % index))) 
        self.is_connected = bool(urllib.unquote(self.sc._request("player connected %i ?" % index))) 

    def get_id(self):
        return self.id
    
    def get_uuid(self):
        return self.uuid

    def get_name(self):
        return self.name

    def set_name(self, name):
        self._request("name %s" % (name))
        self._update(self.index)
    
    def get_ip_address(self):
        return self.ip_address
    
    def get_model(self):
        return self.model
    
    def get_display_type(self):
        return self.display_type
    
    def get_wifi_signal_strength(self):
        return self.wifi_signal_strength
    
    def can_power_off(self):
        return self.can_power_off
    
    def is_player(self):
        return self.is_player
    
    def is_connected(self):
        return self.is_connected

    def get_mode(self):
        self.mode = str(self._request("mode ?"))
        return self.mode
    
    def get_time(self):
        self.time = int(self._request("time ?"))
        return self.time
    
    def get_power_state(self):
        state = int(self._request("power ?"))
        self.power_state = (state != 0)
        return self.power_state
    
    def set_power_state(self, state):
        self._request("power %i" % (int(state)))
        self.get_power_state()    
               
    def get_volume(self):
        self.volume = int(self._request("mixer volume ?"))
        return self.volume           

    def get_muting(self):
        state = int(self._request("mixer muting ?"))
        self.muting = (state != 0)
        return self.muting

    def set_muting(self, state):
        self._request("mixer muting %i" % (int(state)))
        self.get_muting()
               
    def show(self, line1="", line2="", duration=3, brightness=4, font="standard", centered=False):
        if font=="huge": line1=""
        self._request("show line1:%s line2:%s duration:%i brightness:%i font:%s centered:%i" % (line1, line2, duration, brightness, font, int(centered)))

    def play(self):
        self._request("play")

    def stop(self):
        self._request("stop")

    def pause(self):
        self._request("pause 1")

    def unpause(self):
        self._request("pause 0")

    def toggle(self):
        self._request("pause")
    
    def set_volume(self, volume):
        if volume < 0: volume = 0
        if volume > 100: volume = 100
        self._request("mixer volume %i" % (volume))

    def volume_up(self, amount):
        self._request("mixer volume +%i" % (amount))
        self.get_volume()

    def volume_down(self, amount):
        self._request("mixer volume -%i" % (amount))
        self.get_volume()
    
    def mute(self):
        self.set_muting(True)
        
    def unmute(self):
        self.set_muting(False)
    
    def seek_to(self, seconds):
        self._request("time %s" % (self.seconds))
        
    def forward(self, seconds):
        self._request("time +%s" % (self.seconds))        

    def rewind(self, seconds):
        self._request("time -%s" % (self.seconds))   


    # Properties

    id = property(get_id)
    uuid = property(get_uuid)
    name = property(get_name, set_name)
    ip_address = property(get_ip_address)
    model = property(get_model)
    display_type = property(get_display_type)
    wifi_signal_strength = property(get_wifi_signal_strength)
    can_power_off = property(can_power_off)
    is_player = property(is_player)
    is_connected = property(is_connected)
    time = property(get_time)
    mode = property(get_mode)
    power_state = property(get_power_state, set_power_state)   
    volume = property(get_volume, set_volume)   
    muting = property(get_muting, set_muting)  