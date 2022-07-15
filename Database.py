import numpy as np
from IPython.display import Audio
import librosa
import random

dict = {} 
class song_database:
    def init(self, peak_pair, song_ID):
        self.peak_pair = peak_pair
        self.song_ID = song_ID

    def add_song(peak_pair: tuple, fanout_m: np.ndarray, song_ID):
        """ take in a peak pair, 

        Parameters
        ----------
        ((fm, fn, dt), tm) : 
            Path to text file containing favorite food survey responses.
        fanout_m :

        song_ID :

        Returns
        -------
        Dict[tuple, [(tuple)]]
            Dictionary with the key being peak pair and value being list of song-IDs and times associated.
        """
        for (fm, fn, dt), tm in fanout_m:
            if peak_pair(0) not in dict.keys():
                dictionary[peak_pair(0)] = [(song_ID, tm)]
            elif peak_pair(0) in dict.keys():
                dictionary[(fm, fn, dt)].append((song_ID, tm))
    def find_song():
        pass