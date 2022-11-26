# Defining main function
from backend import *


# main is mainly for testing purposes
def main():
    mp3_to_csv('example_3.mp3')
    # data, sample_frame_rate = librosa.load("example_1.mp3")
    #####
    # data, sample_frame_rate = breakdown("example_1.mp3")
    # tiles, timestamp = make_tiles_no_hold(data, sample_frame_rate)
    # t1, ts1, l1 = make_tiles_hold(data, sample_frame_rate)
    # # print(tiles)
    # # print(timestamp)
    # list_to_csv_no_hold(tiles, timestamp)
    # list_to_csv_hold(t1, ts1, l1)

    #####
    # onset_frames = librosa.onset.onset_detect(data, sr=sample_frame_rate, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
    # onset_times = librosa.frames_to_time(onset_frames)
    # print(onset_times)
    # print(onset_frames)
    # print(data[:50])
    # print(sample_frame_rate)
    #
    # # tempo, beat_times = librosa.beat.beat_track(data, sr=sample_frame_rate, start_bpm=60, units='time')
    #####
    # l = ['l', 'r', 'u', 'd']
    # print(random.choice(l))
    # print(tempo)
    # print(beat_times)
    # print(type(beat_times))
    # print(type(data))

    # print(type(data))
    # print(len(data))
    # print(np.shape(data))
    # time_e = np.linspace(start=0, stop=len(data)/sample_frame_rate, num=len(data))
    # print(time_e)
    # print(len(time_e))
    # # this tells me the length of music, sample 3 is about 2min 11 sec
    # dur = librosa.get_duration(data, sample_frame_rate)
    # print(dur)
    # f = wave.open("example_1.wav")
    # # fr = Wave_read.getframerate(f)
    # # # farr = Wave_read.readframes(10)
    # rate, data1 = wav.read('example_1.wav')
    # print(rate)
    # print(data1[:100])
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