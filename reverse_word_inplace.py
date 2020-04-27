# https://www.interviewcake.com/question/python3/reverse-words?course=fc1&section=array-and-string-manipulation
import unittest


def reverse_list(message, i, j):
    while i <= j:
        temp = message[i]
        message[i] = message[j]
        message[j] = temp
        i += 1
        j -= 1


def reverse_words(message):
    if len(message) <= 1:
        return message

    message.reverse()

    i = 0
    j = 0

    while j < len(message):
        if message[j] == " ":
            reverse_list(message, i, j - 1)
            i = j + 1
        j += 1
    reverse_list(message, i, j - 1)


class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)

unittest.main(verbosity=2)