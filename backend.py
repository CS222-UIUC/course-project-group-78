# import all libraries that we need
import random
from random import sample
import math
import librosa
import pandas as pd
import numpy as np
import scipy as sp

def breakdown(file):
    '''
    a function that takes in a mp3 file and break it down
    :return: an array of frequencies
    '''
    data, sample_rate = librosa.load(file, sr=None)
    return data, sample_rate # returns NumPy array

def make_tiles_no_hold(data, sr):
    tempo, beat_times = librosa.beat.beat_track(data, sr=sr, start_bpm=60, units='time')
    timestamp = beat_times.tolist()
    l = ['l', 'r', 'u', 'd']
    tiles = []
    for i in range(len(timestamp)):
        tiles.append(random.choice(l))
    return tiles, timestamp

def make_tiles_hold(y):
    return 0

def list_to_csv(tiles, timestamp):
    d = {'tiles': tiles, 'timestamp': timestamp}
    df = pd.DataFrame(data=d)
    df.to_csv('output.csv')

# def freq_to_tile(freqs):
#     tiles = []
#     curr_note = 0
#     len = 0;
#     curr_note = freqs[0]
#     for i in range(len(freqs)):
#         if(abs(freqs[i]-curr_note) <= 2**(1/12.0) and i < len(freqs)-1):
#             len += 1;
#             #if the note is the same, just increment length
#         else:
#             if(abs(curr_note) < 0.15):
#                 tiles.append([0, len])
#                 #if < 0.15, it's a rest
#                 #for rest the tile value is 0
#             else if(freqs[i] < curr_note):
#                 #move the new tile one to the left
#                 #if it's the leftmost(1) tile, move to 4.
#                 if(tiles[len(tiles)-1][0] == 1):
#                     tiles.append([4,len])
#                 else:
#                     tiles.append((tiles[len(tiles)-1][0]-1, len))
#             else:
#                 #similar here but if it's the most right, move to 1
#                 if(tiles[len(tiles)-1][0] == 4):
#                     tiles.append([1,len])
#                 else:
#                     tiles.append((tiles[len(tiles)-1][0]+1, len))
#             curr_note = freqs[i]
#             len = 1;
#     return tiles

# figure out how to take mp3 file from front end

# function that takes in 1 parameter (music mp3 file)
# def analyze_music():
#
#     '''
#     call helpers and stuff
#     :return: a file of our actual beatmap
#     '''
#
# from os import path
# from pydub import AudioSegment

# def convert_to_wav(src):
#     # files
#     dst = "mp3ToWav.wav"
#     # convert wav to mp3
#     sound = AudioSegment.from_mp3(src)
#     sound.export(dst, format="wav")
#     return dst


# helpers





# figure out how to send file back to frontend
