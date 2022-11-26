# import all libraries that we need
import random
import librosa
import pandas as pd

def breakdown(file):
    '''
    a function that takes in a mp3 file and break it down
    :return: an array of frequencies
    '''
    data, sample_rate = librosa.load(file)
    return data, sample_rate # returns NumPy array

def make_tiles_no_hold(data, sr):
    onset_frames = librosa.onset.onset_detect(data, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1,
                                              post_max=1)
    onset_times = librosa.frames_to_time(onset_frames)
    onset_times_return = []
    for i in range(1, len(onset_times)):
        if onset_times[i] - onset_times[i - 1] > 0.15:
            onset_times_return.append(onset_times[i])

    l = ['l', 'r', 'u', 'd']
    tiles = []
    for i in range(len(onset_times_return)):
        tiles.append(random.choice(l))
    return tiles, onset_times_return
def make_tiles_hold(data, sr):
    onset_frames = librosa.onset.onset_detect(data, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1,
                                              post_max=1)
    onset_times = librosa.frames_to_time(onset_frames)
    onset_times_return = []
    length = []
    note_length = 1
    for i in range(1, len(onset_times)):
        if onset_times[i] - onset_times[i - 1] > 0.15:
            onset_times_return.append(onset_times[i])
            length.append(note_length)
            note_length = 1
        else:
            note_length += 1

    l = ['l', 'r', 'u', 'd']
    tiles = []
    for i in range(len(onset_times_return)):
        tiles.append(random.choice(l))
    return tiles, onset_times_return, length

def list_to_csv_no_hold(tiles, timestamp):
    d = {'tiles': tiles, 'timestamp': timestamp}
    df = pd.DataFrame(data=d)
    df.to_csv('no_hold_output.csv')

def list_to_csv_hold(tiles, timestamp, length):
    d = {'tiles': tiles, 'timestamp': timestamp, 'note length': length}
    df = pd.DataFrame(data=d)
    df.to_csv('hold_output.csv')

def beat_generation(data, sr):
    tempo, beat_times = librosa.beat.beat_track(data, sr=sr, start_bpm=60, units='time')
    timestamp = beat_times.tolist()
    timestamp_return = [timestamp[0]]
    for i in range(1, len(timestamp)):
        if timestamp[i] - timestamp_return[i - 1] > 0.33:
            timestamp_return.append(timestamp[i])

    l = ['l', 'r', 'u', 'd']
    tiles = []
    for i in range(len(timestamp_return)):
        tiles.append(random.choice(l))
    return tiles, timestamp_return

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
