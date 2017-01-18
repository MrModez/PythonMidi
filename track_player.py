import _thread
import threading
import time

import mido
from music21 import *
from mido import Message

exitFlag = 0


class TrackPlayer(threading.Thread):

    def __init__(self, port, track):
        threading.Thread.__init__(self)
        self.track = track
        self.events = track.events
        self.port = port

    def run(self):
        play(self.port, self.events)


def play(port, events):
    for event in events:
        print(str(event) + "\n")
        if event.type == "NOTE_ON" or event.type == "NOTE_OFF":
            ev_type = event.type.lower()
            ms = Message(ev_type, note=event.pitch, velocity=event.velocity, channel=event.channel)
            port.send(ms)
        if event.type == "DeltaTime":
            time.sleep(event.time / 200)
