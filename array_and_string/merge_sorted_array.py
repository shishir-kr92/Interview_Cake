import unittest

'''
###################################################################################################################
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our
Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists.
Write a function to merge our lists of orders into one sorted list.

###################################################################################################################
For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print merge_lists(my_list, alices_list)
# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

###################################################################################################################
LINK :-
https://www.interviewcake.com/question/python/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation
###################################################################################################################
'''


def merge_lists(x, y):
    i = 0
    j = 0
    k = 0

    if len(x) == 0 and len(y) == 0:
        return list()

    new_list = [-1 for _ in range(len(x) + len(y))]

    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            new_list[k] = x[i]
            i += 1
        else:
            new_list[k] = y[j]
            j += 1
        k += 1

    # k -= 1

    # if more element in x
    while i < len(x):
        new_list[k] = x[i]
        i += 1
        k += 1

    # if more element in y
    while j < len(y):
        new_list[k] = y[j]
        j += 1
        k += 1
    return new_list


class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
