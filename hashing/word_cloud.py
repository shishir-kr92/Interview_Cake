import unittest

'''
###################################################################################################################
To do this, you'll need data. Write code that takes a long string and builds its word cloud data in
a dictionary ,where the keys are words and the values are the number of times the words occurred.

Think about capitalized words. For example, look at these sentences:

'After beating the eggs, Dana read the next step:'
'Add milk and eggs, then add flour and sugar.'

What do we want to do with "After", "Dana", and "add"? In this example, your final dictionary should
include one "Add" or "add" with a value of 22. Make reasonable (not necessarily perfect) decisions
about cases like "After" and "Dana".

Assume the input will only contain words and standard punctuation.
###################################################################################################################
LINK :-
https://www.interviewcake.com/question/python3/word-cloud?course=fc1&section=hashing-and-hash-tables
###################################################################################################################
'''


class WordCloudData:
    def __init__(self, input):
        self.words_to_counts = self.split_words(input)

    def clean_word(self, word):
        start_index = 0
        end_index = len(word) - 1

        # remove special character from beginning
        while start_index < len(word) and not word[start_index].isalpha():
            start_index += 1

        # remove special character from ending
        while end_index >= 0 and not word[end_index].isalpha():
            end_index -= 1

        return word[start_index:end_index + 1]

    def get_tokenized_string(self, s):
        separator_set = (" ", ":", ",", ".")

        i = 0
        j = 0

        while j < len(s):
            if s[j] in separator_set:
                word = s[i:j]
                # print(word)
                if len(word) > 0:
                    # word_list.append(self.clean_word(word))
                    yield self.clean_word(word)
                i = j + 1
            j += 1
        yield self.clean_word(s[i:j])

    def split_words(self, s):
        lookup_table = dict()
        # delimiter_found = False

        # start_index = 0
        for word in self.get_tokenized_string(s):
            if not word:
                continue
            elif word in lookup_table:
                lookup_table[word] += 1
            elif word.lower() in lookup_table:
                lookup_table[word.lower()] += 1
            elif word.capitalize() in lookup_table:
                lookup_table[word] = lookup_table[word.capitalize()] + 1
                del lookup_table[word.capitalize()]
            else:
                lookup_table[word] = 1
        return lookup_table


def main():
    input_word_list = [
        'I like cake',
        'Chocolate cake for dinner and pound cake for dessert',
        'Strawberry short cake? Yum!',
        'Dessert - mille-feuille cake',
        "Allie's Bakery: Sasha's Cakes",
        'Mmm...mmm...decisions...decisions'
    ]
    for word in input_word_list:
        print("=================================================")
        print(word)
        result = WordCloudData(word).words_to_counts
        print(result)
        print("=================================================")


# Tests
# There are lots of valid solutions for this one. You
# might have to edit some of these tests if you made
# different design decisions in your solution.

class Test(unittest.TestCase):

    def test_simple_sentence(self):
        input = 'I like cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'I': 1, 'like': 1, 'cake': 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = 'Chocolate cake for dinner and pound cake for dessert'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {
            'and': 1,
            'pound': 1,
            'for': 2,
            'dessert': 1,
            'Chocolate': 1,
            'dinner': 1,
            'cake': 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = 'Strawberry short cake? Yum!'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = 'Dessert - mille-feuille cake'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'cake': 1, 'Dessert': 1, 'mille-feuille': 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = 'Mmm...mmm...decisions...decisions'

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {'mmm': 2, 'decisions': 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"

        word_cloud = WordCloudData(input)
        actual = word_cloud.words_to_counts

        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)