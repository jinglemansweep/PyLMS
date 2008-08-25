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
    
    # internals
    
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
        self.track_genre = None
        self.track_artist = None
        self.track_album = None
        self.track_title = None
        self.track_duration = None
        self.track_remote = None
        self.track_current_title = None
        self.track_path = None
        self._update(index)

    def __repr__(self):
        return self.id
    
    def _request(self, command_string):
        """Executes Telnet Request via SqueezeCenter"""
        return self.sc._request("%s %s" % (self.id, command_string))
    
    def _update(self, index):
        """Update Player Properties from SqueezeCenter"""
        self.index = index
        self.id = str(urllib.unquote(self.sc._request("player id %i ?" % index)))
        self.uuid = str(urllib.unquote(self.sc._request("player uuid %i ?" % index)))
        self.name = str(urllib.unquote(self.sc._request("player name %i ?" % index)))    
        self.ip_address = str(urllib.unquote(self.sc._request("player ip %i ?" % index)))    
        self.model = str(urllib.unquote(self.sc._request("player model %i ?" % index)))   
        self.display_type = str(urllib.unquote(self.sc._request("player displaytype %i ?" % index)))
        self.can_power_off = bool(urllib.unquote(self.sc._request("player canpoweroff %i ?" % index))) 
        self.is_player = bool(urllib.unquote(self.sc._request("player isplayer %i ?" % index))) 
        self.is_connected = bool(urllib.unquote(self.sc._request("player connected %i ?" % index))) 

    def get_id(self):
        """Get Player ID"""
        return self.id
    
    def get_uuid(self):
        """Get Player UUID"""
        return self.uuid

    def get_name(self):
        """Get Player Name"""
        return self.name

    def set_name(self, name):
        """Set Player Name"""
        self._request("name %s" % (name))
        self._update(self.index)
    
    def get_ip_address(self):
        """Get Player IP Address"""
        return self.ip_address
    
    def get_model(self):
        """Get Player Model String"""
        return self.model
    
    def get_display_type(self):
        """Get Player Display Type String"""
        return self.display_type
    
    def get_wifi_signal_strength(self):
        """Get Player WiFi Signal Strength"""
        self.wifi_signal_strength = self._request("signalstrength ?")
        return self.wifi_signal_strength

    def has_permission(self, request_terms):
        """Check Player User Permissions"""
        request_terms = urllib.quote(request_terms)
        granted = int(self._request("can %s ?" % (request_terms)))
        return (granted == 1)
    
    def get_pref_value(self, name, namespace=None):
        """Get Player Preference Value"""
        pref_string = ""
        if namespace:
            pref_string += namespace + ":"
        pref_string += name
        value = self._request("pref %s ?" % (pref_string))
        return value

    def set_pref_value(self, name, value, namespace=None):
        """Set Player Preference Value"""
        pref_string = ""
        if namespace:
            pref_string += namespace + ":"
        pref_string += name
        value = urllib.quote(value)
        valid = self._request("pref validate %s %s" % (pref_string, value))
        if "valid:1" in valid:
            self._request("pref %s %s" % (pref_string, value))
            return True
        else:
            return False
    
    def can_power_off(self):
        """Player Can Power Off?"""
        return self.can_power_off
    
    def is_player(self):
        """Real Player?"""
        return self.is_player
    
    def is_connected(self):
        """Player Connected?"""
        return self.is_connected

    def get_mode(self):
        """Get Player Mode"""
        self.mode = str(self._request("mode ?"))
        return self.mode
    
    def get_time_elapsed(self):
        """Get Player Time Elapsed"""
        self.time = float(self._request("time ?"))
        return self.time
    
    def get_time_remaining(self):
        """Get Player Time Remaining"""
        if self.get_mode() == "play":
            remaining = self.get_track_duration() - self.get_time_elapsed()
            return remaining
        else:
            return 0
    
    def get_power_state(self):
        """Get Player Power State"""
        state = int(self._request("power ?"))
        self.power_state = (state != 0)
        return self.power_state
    
    def set_power_state(self, state):
        """Set Player Power State"""
        self._request("power %i" % (int(state)))
        self.get_power_state()    
               
    def get_volume(self):
        """Get Player Volume"""
        self.volume = int(self._request("mixer volume ?"))
        return self.volume           

    def get_muting(self):
        """Get Player Muting Status"""
        state = int(self._request("mixer muting ?"))
        self.muting = (state != 0)
        return self.muting

    def set_muting(self, state):
        """Set Player Muting Status"""
        self._request("mixer muting %i" % (int(state)))
        self.get_muting()
    
    def get_track_genre(self):
        """Get Players Current Track Genre"""
        self.track_genre = str(self._request("genre ?"))
        return self.track_genre

    def get_track_artist(self):
        """Get Players Current Track Artist"""
        self.track_album = str(self._request("artist ?"))
        return self.track_artist
    
    def get_track_album(self):
        """Get Players Current Track Album"""
        self.track_album = str(self._request("album ?"))
        return self.track_album
    
    def get_track_title(self):
        """Get Players Current Track Title"""
        self.track_title = str(self._request("title ?"))
        return self.track_title
    
    def get_track_duration(self):
        """Get Players Current Track Duration"""
        self.track_duration = float(self._request("duration ?"))
        return self.track_duration    
    
    def get_track_remote(self):
        """Is Players Current Track Remotely Hosted?"""
        remote = int(self._request("remote ?"))
        self.track_remote = (remote != 0)
        return self.track_remote  

    def get_track_current_title(self):
        """Get Players Current Track Current Title"""
        self.track_current_title = str(self._request("current_title ?"))
        return self.track_current_title

    def get_track_path(self):
        """Get Players Current Track Path"""
        self.track_path = str(self._request("path ?"))
        return self.track_path
    
    # actions
               
    def show(self, line1="", line2="", duration=3, brightness=4, font="standard", centered=False):
        """Displays text on Player display"""
        if font=="huge": line1=""
        line1, line2 = urllib.quote(line1), urllib.quote(line2)
        self._request("show line1:%s line2:%s duration:%i brightness:%i font:%s centered:%i" % (line1, line2, duration, brightness, font, int(centered)))

    def play(self):
        """Play"""
        self._request("play")

    def stop(self):
        """Stop"""
        self._request("stop")

    def pause(self):
        """Pause On"""
        self._request("pause 1")

    def unpause(self):
        """Pause Off"""
        self._request("pause 0")

    def toggle(self):
        """Play/Pause Toggle"""
        self._request("pause")
    
    def set_volume(self, volume):
        """Set Player Volume"""
        if volume < 0: volume = 0
        if volume > 100: volume = 100
        self._request("mixer volume %i" % (volume))

    def volume_up(self, amount=5):
        """Increase Player Volume"""
        self._request("mixer volume +%i" % (amount))
        self.get_volume()

    def volume_down(self, amount=5):
        """Decrease Player Volume"""
        self._request("mixer volume -%i" % (amount))
        self.get_volume()
    
    def mute(self):
        """Mute Player"""
        self.set_muting(True)
        
    def unmute(self):
        """Unmute Player"""
        self.set_muting(False)
    
    def seek_to(self, seconds):
        """Seek Player"""
        self._request("time %s" % (self.seconds))
        
    def forward(self, seconds):
        """Seek Player Forward"""
        self._request("time +%s" % (self.seconds))        

    def rewind(self, seconds):
        """Seek Player Backwards"""
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
    time_elapsed = property(get_time_elapsed)
    time_remaining = property(get_time_remaining)
    mode = property(get_mode)
    power_state = property(get_power_state, set_power_state)   
    volume = property(get_volume, set_volume)   
    muting = property(get_muting, set_muting)  
    track_genre = property(get_track_genre)
    track_artist = property(get_track_artist)
    track_title = property(get_track_title)
    track_duration = property(get_track_duration)
    track_remote = property(get_track_remote)
    track_current_title = property(get_track_current_title)
    track_path = property(get_track_path)