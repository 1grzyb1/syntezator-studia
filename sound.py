import pyaudio
import numpy as np
from numpy import ndarray
from sound_wave import SoundWave as sw
from wave import Wave
import threading
from scipy import signal


class Sound:
    def __init__(self, attack, decay, sustain, release, wave_type):
        self.p = pyaudio.PyAudio()
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
        self.wave_type = wave_type
        self.playing = True
        self.duration = 0.01

    def play(self, frequency):

        fs: int = 100100
        f: float = frequency
        self.duration: float = 1 / f

        time: ndarray = np.arange(fs * self.duration)

        angle = 2 * np.pi * time * f / fs

        self.samples = np.sin(angle)

        if self.wave_type == Wave.SQUARE:
            self.samples = signal.square(angle)
        elif self.wave_type == Wave.SAWTOOTH:
            self.samples = signal.sawtooth(angle)
        elif self.wave_type == Wave.TRIANGLE:
            self.samples = signal.sawtooth(angle, 0.5)

        self.stream = self.p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

        wave = np.array([0])
        cycles = 1
        max_range = int(cycles * self.attack / self.duration)

        #attack
        for i in range(0, max_range, cycles):
            sound = i / max_range * self.samples.astype(np.float32)
            wave = np.concatenate([wave, sound])
            self.stream.write(sound)

        cycles = ((1 - self.sustain)*self.duration)/self.decay
        sound
        #decay
        for i in np.arange(1, self.sustain, -cycles):
            sound = i * self.samples.astype(np.float32)
            wave = np.concatenate([wave, sound])
            self.stream.write(sound)

        self.wave = wave
        #sustain
        threading.Thread(target=self._decay, args=(self.stream, sound)).start()

    def stop(self):
        self.playing = False

        cycles = (self.sustain * self.duration) / self.release
        for i in np.arange(self.sustain, 0, -cycles):
            sound = i * self.samples.astype(np.float32)
            self.wave = np.concatenate([self.wave, sound])
            try:
                self.stream.write(sound)
                if self.stream.is_active():
                    self.stream.stop_stream()
                    self.stream.close()

                self.p.terminate()

                sw.show(self.wave)
            except OSError as e:
                print(f"Error writing to stream: {e}")
                break

    def _decay(self, stream, sound):
        while self.playing:
            try:
                stream.write(sound)
                self.wave = np.concatenate([self.wave, sound])
            except OSError as e:
                print(f"Error writing to stream: {e}")
                break