import numpy as np
from IPython.display import Audio
import librosa
import random

def random_splice(song_path, snippets, duration):
    samples, sampling_rate = librosa.load(song_path, sr=44100, mono=True, duration=180)
    length = len(samples) #2138112
    clips = []
    for i in range(snippets):
        end = duration * 44100 #1323000
        factor = random.randint(0, (length - end))
        clips.append(samples[(0+factor):(end+factor)])
    return clips