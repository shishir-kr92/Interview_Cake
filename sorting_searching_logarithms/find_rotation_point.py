import unittest


def find_rotation_point(word_list):
    first = word_list[0]
    low = 0
    high = len(word_list) - 1

    while low < high:
        mid = low + abs((high - low) / 2)

        if first > word_list[mid]:
            high = mid

        elif first < word_list[mid]:
            low = mid

        if low + 1 == high:
            return high


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)
        
unittest.main(verbosity=3)