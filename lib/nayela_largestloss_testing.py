from unittest import TestCase
import random
from nayela_largestloss import *

class TestLargestLoss(TestCase):

  def test_largest_loss(self):
    # pricesLst = random.sample(range(1, 5000), 3500) - old code

    # Test to check that 0 is returned if there is only one value in the list
      pricesLst1 = [27]
      calculation = largest_loss(pricesLst1)
      self.assertEqual(calculation, 0)


      # Test to check function works in 'normal' range of numbers
      pricesLst2 = [1, 100, 250, 20000, 3000, 543, 27, 07, 89, 19, 5867, 220]
      calculation = largest_loss(pricesLst2)
      self.assertEqual(calculation, 19750)

TestLargestLoss("test_largest_loss")

### Old, poorly indented code ###
# class TestLargestLoss(TestCase):


#   def test_largest_loss(self):
#     # pricesLst = random.sample(range(1, 5000), 3500) - old code

#     # Test to check that 0 is returned if there is only one value in the list
#     pricesLst1 = [27]
#     calculation = largest_loss(pricesLst1)
#     self.assertEqual(calculation, 0)


#     # Test to check function works in 'normal' range of numbers
#     pricesLst2 = [1, 100, 250, 20000, 3000, 543, 27, 07, 89, 19, 5867, 220]
#     calculation = largest_loss(pricesLst2)
#     self.assertEqual(calculation, 19750)
