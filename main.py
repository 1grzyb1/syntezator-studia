from sound import Sound
from wave import Wave
import time

from wave import Wave

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    sound_variables = {}
    song_notes = []

    for line in lines:
        line = line.strip()  # remove newline character
        if ':' in line:
            variable, value = line.split(':')
            variable = variable.strip()
            value = value.strip()

            if variable == 'Wave':
                value = Wave[value.upper()]

            sound_variables[variable] = value
        else:
            song_notes.append(line)

    return sound_variables, song_notes

notes = {"C": 65.41,
         "D": 73.42,
         "E": 82.41,
         "F": 87.31,
         "G": 98.00,
         "A": 110.00,
         "B": 123.47}

sound_variables, song_notes = read_file('song.txt')

attack = float(sound_variables['attack'])
decay = float(sound_variables['decay'])
sustain = float(sound_variables['sustain'])
release = float(sound_variables['release'])
wave_type = sound_variables['Wave']

def play(note, delay):
    sound = Sound(0.05, 0.05, 0.5, 0.05, Wave.TRIANGLE)
    sound.play(note)
    time.sleep(delay)
    sound.stop()


sound = Sound(attack, decay, sustain, release, wave_type)

for note in song_notes:
    play(notes.get(note), 0.1)