# import all libraries that we need
from random import sample
import librosa
import numpy as np
import scipy as sp

# figure out how to take mp3 file from front end

# function that takes in 1 parameter (music mp3 file)
def analyze_music():

    '''
    call helpers and stuff
    :return: a file of our actual beatmap
    '''


# helpers

def breakdown(file):
    '''
    a function that takes in an mp3 file and break it down
    :return: an array of frequencies
    '''
    data, sample_rate = librosa.load(file, sr=None)
    return data, sample_rate # returns NumPy array

def analyze():
    '''
    takes in an array of frequencies and analyze the music
    :return: our map in some kind of data type - tbd
    '''


def convert():
    '''
    takes in our map and convert it into an actual file
    :return: actual beatmap file
    '''


# figure out how to send file back to frontend