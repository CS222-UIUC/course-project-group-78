import unittest
import wave

from backend import *
from wave import *

# test for successful conversion from mp3 to wav file
# Use iTunes on Mac, listen and compare the music

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

def test_breakdown():
    # this array below is generated using
    # is there a way to test this????
    breakdown_answer1 = np.array(
            [0.0000000e+00, 0.0000000e+00, 0.0000000e+00, 0.0000000e+00, -1.5258789e-05, 4.5776367e-05, -6.1035156e-05,
             6.1035156e-05, -3.0517578e-05, -1.5258789e-05])
    breakdown_to_test1, fr1 = breakdown("example_1_test.mp3")
    # true framerate is genertated by using getframerate() on the wav file of the example_1_test
    e1wav = wave.open("example_1_test.wav")
    fr1_true = Wave_read.getframerate(e1wav)
    assert fr1_true == fr1
    assert (len(breakdown_to_test1) > 0)
    assert np.allclose(breakdown_to_test1[:10], breakdown_answer1)

    print("example1 passed")

    breakdown_answer3 = np.array(
        [-0.0005188, -0.00079346, -0.00083923, -0.00097656, -0.00106812, -0.00120544, -0.00125122, -0.00132751, -0.00143433, -0.00143433])
    breakdown_to_test3, fr3 = breakdown("example_3_test.mp3")
    e3wav = wave.open("example_3_test.wav")
    fr3_true = Wave_read.getframerate(e3wav)
    assert fr3_true == fr3
    assert (len(breakdown_to_test3) > 0)
    assert np.allclose(breakdown_to_test3[:10], breakdown_answer3)
    print("example3 passed")

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
    #     map_size_to_test = generatemap(freq, wave, amp)
    #     self.assertEqual(map_size_to_test, map_size_answer)  # add assertion here
    #
    # def test_tile_length(self):
    #     tile_length_answer = 0 '''a float, represents how long the tiles are'''
    #     tile_length_to_test = generatetile(freq[i], wave[i], amp[i])
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
    #     score_to_test = getscore()
    #     self.assertEqual(score_to_test, score_answer)  # add assertion here


if __name__ == '__main__':
   #  unittest.main()
    test_breakdown()
    print("Everything passed")
