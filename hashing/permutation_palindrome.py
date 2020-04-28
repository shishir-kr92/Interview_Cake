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


def has_palindrome_permutation_old(the_string):
    '''
        Memory overflow exception can occur
    '''
    char_dict = dict()
    found_mid_char = False

    if len(the_string) <= 1:
        return True

    for c in the_string:
        try:
            char_dict[c] += 1
        except KeyError:
            char_dict[c] = 1

    for key, value in char_dict.items():
        if value % 2 == 0:
            continue
        elif not found_mid_char and value % 2 == 1:
            found_mid_char = True
        else:
            return False
    return True


def has_palindrome_permutation(the_string):
    '''
        for any key c
        True -> even
        False -> odd
    '''
    lookup_table = dict()
    odd_count_char = 0

    for c in the_string:
        try:
            if lookup_table[c]:
                lookup_table[c] = False
            else:
                lookup_table[c] = True
        except KeyError:
            lookup_table[c] = False
    for key, value in lookup_table.items():
        if not value:
            odd_count_char += 1
        if odd_count_char > 1:
            return False
    return True
# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('civic')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)

unittest.main(verbosity=2)
