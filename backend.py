# import all libraries that we need
from random import sample
import math
import librosa
import numpy as np
import scipy as sp

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

def freq_to_tile(freqs):
    min = 10000000
    tiles = []
    curr_note = 0
    len = 0;
    for i in range(len(freqs)):
        if(abs(freqs[i]-curr_note) <= 2**(1/12.0) and i < len(freqs)-1 and i > 0):
            len += 1;
        else:
            if(len < min):
                min = len
            if(freqs[i] < curr_note):
                if(tiles[len(tiles)-1][0] == 1):
                    tiles.append([4,len])
                else:
                    tiles.append((tiles[len(tiles)-1][0]-1, len))
            else:
                if(tiles[len(tiles)-1][0] == 4):
                    tiles.append([1,len])
                else:
                    tiles.append((tiles[len(tiles)-1][0]+1, len))
            curr_note = freqs[i]
            len = 1;
    return tiles


# helpers

def breakdown(file):
    '''
    a function that takes in a mp3 file and break it down
    :return: an array of frequencies
    '''
    data, sample_rate = librosa.load(file, sr=None)
    return data, sample_rate # returns NumPy array



# figure out how to send file back to frontend
