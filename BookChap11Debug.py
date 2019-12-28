import unittest

# def get_fine_name(fn,ln):
#     fname = fn + ' ' +ln
#     return fname

from names import get_fine_name

# print("enter 'q' to quit")
#
# while True:
#     first = input("first name:")
#     if first == 'q':
#         break
#     last = input("last name:")
#     if last == 'q':
#         break
#
#     fine_name = get_fine_name(first, last)
#
#     print("\n fine name is " + fine_name)

class NamesTestCases(unittest.TestCase):
    def test_fine_name(self):
        fine_name = get_fine_name('gag','dfd')
        self.assertEqual(fine_name,'Gag Dfd')

##### see book for setUp()