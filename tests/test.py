import unittest

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
#     '''
#     # suppose my wav to wavelength function is called wavelength and follows the same convention for frequencies and amplitude
#     or I could do something like wavelength_to_test, frequencies_to_test, amplitude_to_test = convert(mp3 file)
#     '''
#     def test_wavelength(self):
#         wavelength_answer = []
#         wavelength_to_test = wavelength(mp3 file)
#         self.assertEqual(wavelength_to_test, wavelength_answer)  # add assertion here
#
#     def test_frequencies(self):
#         frequencies_answer = []
#         frequencies_to_test = frequencies(mp3 file)
#         self.assertEqual(frequencies_to_test, frequencies_answer)  # add assertion here
#
#     def test_amplitude(self):
#         amplitude_answer = []
#         amplitude_to_test = amplitude(mp3 file)
#         self.assertEqual(amplitude_to_test, amplitude_answer)  # add assertion here
#     '''
#     based on how we implement the algorithm, testing blocks might be different
#     '''
#     def test_map_size(self):
#         map_size_answer = 0 '''an integer, represents how many tiles we have'''
#         map_size_to_test = generatemap(freq, wave, amp)
#         self.assertEqual(map_size_to_test, map_size_answer)  # add assertion here
#
#     def test_tile_length(self):
#         tile_length_answer = 0 '''a float, represents how long the tiles are'''
#         tile_length_to_test = generatetile(freq[i], wave[i], amp[i])
#         self.assertEqual(tile_length_to_test, tile_length_answer)  # add assertion here
#
#     def test_hit(self):
#         hit_answer = False '''a boolean, represents the scores'''
#         hit_to_test = '''check input? how to convert click to signals real time'''
#         '''or should we just try to see that on frontend'''
#         self.assertEqual(hit_to_test, hit_answer)  # add assertion here
#
#     def test_score(self):
#         score_answer = 0 '''an int, represents the scores'''
#         score_to_test = getscore()
#         self.assertEqual(score_to_test, score_answer)  # add assertion here
#
# if __name__ == '__main__':
#     unittest.main()
