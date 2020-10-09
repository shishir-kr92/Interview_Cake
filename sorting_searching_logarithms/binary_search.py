import unittest


def binary_search(num_list, target):
    u = len(num_list)
    l = 0


    while True:
        if l + 1 > u:
            break

        mid = l + (u - l) // 2

        if num_list[mid] == target:
            return True
        elif num_list[mid] > target:
            u = mid - 1
        else:
            l = mid + 1
    return False


# Tests
class Test(unittest.TestCase):

    def test_element_not_present(self):
        result = binary_search([2, 4], 1)
        self.assertFalse(result)

    def test_empty_list(self):
        result = binary_search([], 1)
        self.assertFalse(result)

    def test_number_present_at_the_end(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)
        self.assertTrue(result




unittest.main(verbosity=2)