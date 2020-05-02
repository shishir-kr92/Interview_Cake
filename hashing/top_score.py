import unittest


'''
###################################################################################################################
Write an efficient function that checks whether any permutation of an input string is a palindrom
You can assume the input string only contains lowercase letters
Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False

###################################################################################################################
LINK :-
https://www.interviewcake.com/question/python3/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
###################################################################################################################
'''


def sort_scores(unsorted_scores, highest_possible_score):
    lookup_array = [0 for i in range(highest_possible_score + 1)]

    for i in unsorted_scores:
        lookup_array[i] += 1

    k = 0
    for i in range(highest_possible_score, 0, -1):
        while lookup_array[i] > 0:
            unsorted_scores[k] = i
            lookup_array[i] -= 1
            k += 1
    return unsorted_scores

# Tests

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

    def test_all_repeated_scores(self):
        actual = sort_scores([10, 10, 10, 10, 10], 100)
        expected = [10, 10, 10, 10, 10]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)