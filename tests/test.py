from backend import *

# test for successful conversion from mp3 to wav file
# Use iTunes on Mac, listen and compare the music


"""
Below is a test for breakdown()
There really is not much to test for this function, as it is literally just Librosa library's load function
Thus, I am just checking if the conversion was successful by checking the length of breakdown data array
"""


def test_breakdown():
    breakdown_to_test1, fr1 = breakdown("example_1_test.mp3")
    # checking the length of breakdown data array
    assert (len(breakdown_to_test1) > 0)
    print("example1 breakdown passed")

    breakdown_to_test3, fr3 = breakdown("example_3_test.mp3")
    # checking the length of breakdown data array
    assert (len(breakdown_to_test3) > 0)
    print("example3 breakdown passed")


"""
Below is a test for make_tiles_no_hold
I want to make sure:
1. the length of tiles list is same as the length of timestamps
2. the last time stamp is smaller or equal to duration
3. the tiles (directions) are randomly generated
"""


def test_make_tiles_no_hold():
    data1, sr1 = breakdown("example_1_test.mp3")
    tiles_to_test1, onset_time_to_test1 = make_tiles_no_hold(data1, sr1)
    tiles_to_test1_1, onset_time_to_test1_1 = make_tiles_no_hold(data1, sr1)
    dur1 = librosa.get_duration(data1, sr1)
    # the length of tiles list is same as the length of timestamps
    assert len(tiles_to_test1) == len(onset_time_to_test1)
    # the last time stamp is smaller or equal to duration
    assert dur1 >= onset_time_to_test1[-1]
    # the tiles (directions) are randomly generated
    assert tiles_to_test1_1 != tiles_to_test1
    print('example1 make tiles no hold passed')
    data3, sr3 = breakdown("example_3_test.mp3")
    tiles_to_test3, onset_time_to_test3 = make_tiles_no_hold(data3, sr3)
    tiles_to_test3_1, onset_time_to_test3_1 = make_tiles_no_hold(data3, sr3)
    dur3 = librosa.get_duration(data3, sr3)
    # the length of tiles list is same as the length of timestamps
    assert len(tiles_to_test3) == len(onset_time_to_test3)
    # the last time stamp is smaller or equal to duration
    assert dur3 >= onset_time_to_test3[-1]
    # the tiles (directions) are randomly generated
    assert tiles_to_test3_1 != tiles_to_test3
    print('example3 make tiles no hold passed')


"""
Below is a test for make_tiles_hold
I want to make sure:
1. the length of tiles list is same as the length of timestamps
2. the last time stamp is smaller or equal to duration
3. the tiles (directions) are randomly generated
4. length of the length of tiles array is the same as the length of tiles list
5. length of each tile is between 1 and 7, or, to be more specific, 1 to 6.6666. In this case, we will use 7
"""


def test_make_tiles_hold():
    data1, sr1 = breakdown("example_1_test.mp3")
    tiles_to_test1, onset_time_to_test1, len1 = make_tiles_hold(data1, sr1)
    tiles_to_test1_1, onset_time_to_test1_1, len1_1 = make_tiles_hold(data1, sr1)
    dur1 = librosa.get_duration(data1, sr1)
    # the length of tiles list is same as the length of timestamps
    assert len(tiles_to_test1) == len(onset_time_to_test1)
    # the last time stamp is smaller or equal to duration
    assert dur1 >= onset_time_to_test1[-1]
    # the tiles (directions) are randomly generated
    assert tiles_to_test1_1 != tiles_to_test1
    # length of the length of tiles array is the same as the length of tiles list
    assert len(len1) == len(tiles_to_test1)
    for i in range(len(len1)):
        # length of each tile is between 1 and 7, or, to be more specific, 1 to 6.6666. In this case, we will use 7
        assert 1 <= len1[i] <= 7
    print('example1 make tiles hold passed')
    data3, sr3 = breakdown("example_3_test.mp3")
    tiles_to_test3, onset_time_to_test3, len3 = make_tiles_hold(data3, sr3)
    tiles_to_test3_1, onset_time_to_test3_1, len3_1 = make_tiles_hold(data3, sr3)
    dur3 = librosa.get_duration(data3, sr3)
    # the length of tiles list is same as the length of timestamps
    assert len(tiles_to_test3) == len(onset_time_to_test3)
    # the last time stamp is smaller or equal to duration
    assert dur3 >= onset_time_to_test3[-1]
    # the tiles (directions) are randomly generated
    assert tiles_to_test3_1 != tiles_to_test3
    # length of the length of tiles array is the same as the length of tiles list
    assert len(len3) == len(tiles_to_test3)
    for i in range(len(len3)):
        # length of each tile is between 1 and 7, or, to be more specific, 1 to 6.6666. In this case, we will use 7
        assert 1 <= len3[i] <= 7
    print('example3 make tiles hold passed')


if __name__ == '__main__':
    test_breakdown()
    test_make_tiles_no_hold()
    test_make_tiles_hold()
    print("Everything passed")


'''
# example code
# import required modules
from os import path
from pydub import AudioSegment

# # assign files
# input_file = "hello.mp3"
# output_file = "result.wav"
# 
# # convert mp3 file to wav file
# sound = AudioSegment.from_mp3(input_file)
# sound.export(output_file, format="wav")
# '''


#
# # wavelength, frequencies, amplitude
#
# class MyTestCase(unittest.TestCase):
'''
    # suppose my wav to wavelength function is called wavelength and follows the same convention for frequencies and amplitude
    or I could do something like wavelength_to_test, frequencies_to_test, amplitude_to_test = convert(mp3 file)
    '''

# def test_frequencies(self):
    #     frequencies_answer = []
    #     frequencies_to_test = frequencies(mp3 file)
    #     self.assertEqual(frequencies_to_test, frequencies_answer)  # add assertion here
    #
# def test_amplitude(self):
    #     amplitude_answer = []
    #     amplitude_to_test = amplitude(mp3 file)
    #     self.assertEqual(amplitude_to_test, amplitude_answer)  # add assertion here
    # '''
    # based on how we implement the algorithm, testing blocks might be different
    # '''
# def test_map_size(self):
    #     map_size_answer = 0 '''an integer, represents how many tiles we have'''
    #     map_size_to_test = generateMap(freq, wave, amp)
    #     self.assertEqual(map_size_to_test, map_size_answer)  # add assertion here
    #
# def test_tile_length(self):
    #     tile_length_answer = 0 '''a float, represents how long the tiles are'''
    #     tile_length_to_test = generateTile(freq[i], wave[i], amp[i])
    #     self.assertEqual(tile_length_to_test, tile_length_answer)  # add assertion here
    #
# def test_hit(self):
    #     hit_answer = False '''a boolean, represents the scores'''
    #     hit_to_test = '''check input? how to convert click to signals real time'''
    #     '''or should we just try to see that on frontend'''
    #     self.assertEqual(hit_to_test, hit_answer)  # add assertion here
    #
# def test_score(self):
    #     score_answer = 0 '''an int, represents the scores'''
    #     score_to_test = getScore()
    #     self.assertEqual(score_to_test, score_answer)  # add assertion here
