import unittest

'''
    here time complexity is O(nlogn), where n is lenght of array
'''


def swap(num_array, i, j):
    t = num_array[i]
    num_array[i] = num_array[j]
    num_array[j] = t


def get_partition(num_array, low, high):
    i = low
    j = low

    pivot = num_array[high - 1]

    while j < high - 1:
        if num_array[j] >= pivot:
            swap(num_array, i, j)
            i += 1
        j += 1
    swap(num_array, i, high - 1)
    # print(low, high)
    return i


def quick_sort(num_array, low, high):
    if low < high:
        partition = get_partition(num_array, low, high)

        quick_sort(num_array, low, partition)
        quick_sort(num_array, partition + 1, high)


def sort_scores(unsorted_score, highest_possible_score):

    quick_sort(unsorted_score,
               0,
               len(unsorted_score))
    return unsorted_score



class Test(unittest.TestCase):

    def test_no_scores(self):
        actual = sort_scores([], 100)
        expected = []
        self.assertEqual(actual, expected)

    def test_one_score(self):
        actual = sort_scores([55], 100)
        expected = [55]
        self.assertEqual(actual, expected)

    def test_two_scores(self):
        actual = sort_scores([30, 60], 100)
        expected = [60, 30]
        self.assertEqual(actual, expected)

    def test_many_scores(self):
        actual = sort_scores([37, 89, 41, 65, 91, 53], 100)
        expected = [91, 89, 65, 53, 41, 37]
        self.assertEqual(actual, expected)

    def test_repeated_scores(self):
        actual = sort_scores([20, 10, 30, 30, 10, 20], 100)
        expected = [30, 30, 20, 20, 10, 10]
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)
