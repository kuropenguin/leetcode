from pprint import pprint
import unittest
import sys

from FourteenDaysStudyPlanToCrackAlgo.answers.binary_search704 import Solution

class BinarySearchTestCase(unittest.TestCase):
    def setUp(self):
      self.solution = Solution()

    def test_success_search(self):
      nums = [-1,0,3,5,9,12]
      target = 9
      target_index = 4
      self.assertEqual(self.solution.search(nums=nums, target=target), target_index, "success")

if __name__ == '__main__':
    unittest.main()
