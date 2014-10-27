import unittest
from numbers import Number
from pattern import Pattern

class PatternTest(unittest.TestCase):

   def test_empty_pattern_matches(self):
      empty = Pattern()
      self.assertTrue(empty.matches())

   def test_single_item_pattern_matches(self):
      is5 = Pattern(5)
      self.assertTrue(is5.matches(5))

   def test_too_many_args_dont_match(self):
      is5 = Pattern(5)
      self.assertFalse(is5.matches(5, 5))

   def test_too_few_args_dont_match(self):
      is5and7 = Pattern(5, 7)
      self.assertFalse(is5and7.matches(5))

   def test_can_mix_and_match_classes_values_and_predicates(self):
      pattern = Pattern(Number, "Hello", lambda num: num % 2 == 0)
      self.assertTrue(pattern.matches(5, "Hello", 4))

if __name__ == '__main__':
   unittest.main()
