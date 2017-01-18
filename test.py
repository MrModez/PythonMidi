import sys
import random
import time

import mido
from music21 import *
import mido.backends.rtmidi
from mido import Message
import rtmidi

from track_player import TrackPlayer

mido.set_backend('mido.backends.rtmidi')
port_name = "LoopBe Internal MIDI 1"

with mido.open_output(port_name, autoreset=True) as port:
    mf = midi.MidiFile()
    mf.open("D://GuitarVad.mid")
    mf.read()

    players = []
    for track in mf.tracks:
        player = TrackPlayer(port, track)
        players.append(player)
        player.start()
    for player in players:
        player.join()
