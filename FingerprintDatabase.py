import numpy as np
from IPython.display import Audio
from SongDatabase import add_song
import librosa
import random
from collections import Counter


class song_database:
   
    def __init__(self):
        
        self.database = {}

    def add_song_fanout(self, fanout_m, song_ID):
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
        self.fanout_m = fanout_m
        self.song_ID = song_ID
        for fm_fn_dt, tm in fanout_m:
            if fm_fn_dt not in self.database:
                self.database[fm_fn_dt] = [(song_ID, tm)]
            else:
                self.database[fm_fn_dt].append((song_ID, tm))

    def add_song(self, fanout_array, song_ID):
        """ take in a peak pair, 
        
        Parameters
        ----------
        ((fm, fn, dt), tm) : 
            Path to text file containing favorite food survey responses.
        fanout_m :
s
        song_ID :

        Returns
            -------
        Dict[tuple, [(tuple)]]
            Dictionary with the key being peak pair and value being list of song-IDs and times associated.
            """
        for i in fanout_array:
            self.add_song_fanout(i, song_ID)

    

    def find_song_fanout(self, fanout_new):
        sample_list = []
        offset = None
        for fm_fn_dt, tm in fanout_new:
            # print(fm_fn_dt)
            # print(fm_fn_dt in self.database.keys())
            if fm_fn_dt in self.database.keys():
                for i in self.database[fm_fn_dt]:
                    offset = i[1] - tm
                    sample_list.append((i[0], offset))
                
        counter = Counter(sample_list)
        # print(counter)
        counter_values = list(counter.values())
        if(len(counter_values) > 1):
            if counter_values[0] == counter_values[1]:
                return None
            else: 
                return counter, offset
        return counter, offset
    
    def find_song(self, fanout_array):
        counter = Counter()
        offset = None
        for i  in fanout_array:
            add = self.find_song_fanout(i)
            if add is not None:
                counter += add[0]
                if offset is None:
                    offset = add[1]
        print(counter)
        trueCount = {}
        keys = list(counter.keys())
        values = list(counter.values())
        for i in range(len(counter)):
            if keys[i][0] not in list(trueCount.keys()):
                trueCount[keys[i][0]] = values[i]
            else:
                trueCount[keys[i][0]] += values[i]
        print(trueCount)
        return list(trueCount.keys())[0], offset