# Defining main function
import wave

from backend import *
import numpy as np
from wave import *
from scipy.io import wavfile as wav
# import librosa


def main():
    # librosa.load("example_1.mp3")
    data, sample_frame_rate = breakdown("example_3.mp3")
    print(data[:10])
    print(sample_frame_rate)
    print(type(data))
    print(len(data))
    print(np.shape(data))
    time_e = np.linspace(start=0, stop=len(data)/sample_frame_rate, num=len(data))
    print(time_e)
    print(len(time_e))
    # this tells me the length of music, sample 3 is about 2min 11 sec
    dur = librosa.get_duration(data, sample_frame_rate)
    print(dur)
    # f = wave.open("example_1.wav")
    # fr = Wave_read.getframerate(f)
    # # farr = Wave_read.readframes(10)
    # rate, data1 = wav.read('example_1.wav')
    # print(rate)
    # print(data1[:10])
    # print(len(data1))
    # tiles = freq_to_tile(data)
    # print(tiles)

    # wave.open(convert_to_wav("example_1.mp3"))
    # fr = Wave_read.getframerate()
    # print(fr)
    print("done")


# Using the special variable
# __name__
if __name__ == "__main__":
    main()