import unittest
from decorators import case, default, _
from duckface import Duckface

class DecoratorsTest(unittest.TestCase):

   def test_base_works(self):
      @default
      def identity(x): 
         return x

      self.assertEqual(identity(3), 3)

   def test_case_works(self):
      @case(42)
      def hey(x):
         return "Forty-two!"

      @default
      def hey(x):
         return "Not forty-two :("

      self.assertEqual(hey(42), "Forty-two!")
      self.assertEqual(hey(31), "Not forty-two :(")

   def test_scoping_rules_work(self):
      # This is to check that the hey defined in the scope of this test is different to the
      # hey() defined in the previous test, as they're in different scopes. If they are, it'll
      # use the prior hey()'s case for a value of 42.

      @default
      def hey(x):
         return "sad"
  
      self.assertEqual(hey(42), "sad")

   def test_methods_work_and_are_scoped_properly(self):
      class A:
         @case(_, 42)
         def hey(self, x):
            return "Yay"
  
         @default
         def hey(self, x):
            return "Boo"
      
      class B:
         @case(_, 42)
         def hey(self, x):
            return "Woo"

         @default
         def hey(self, x):
            return "Bah"

      a = A()
      b = B()
      self.assertEqual(a.hey(42), "Yay")
      self.assertEqual(a.hey(35), "Boo")
      self.assertEqual(b.hey(42), "Woo")
      self.assertEqual(b.hey(35), "Bah")

   def test_can_dispatch_on_ducktypes(self):
      iterable = Duckface("__iter__")

      @case(iterable)
      def flatten(xs): 
        flattened = []
        for x in xs:
          flattened.extend(flatten(x))
        return flattened

      @default
      def flatten(x): return [x]

      self.assertEqual(flatten(flatten([1, 2, (3, 4), 5, ([range(6, 9)], 9), 0])), 
                       [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])


   def test_class_methods_work_and_are_scoped_properly(self):
      class A:
         @case(42)
         def hey(x):
            return "Yay"
  
         @default
         def hey(x):
            return "Boo"
      
      class B:
         @case(42)
         def hey(x):
            return "Woo"

         @default
         def hey(x):
            return "Bah"

      self.assertEqual(A.hey(42), "Yay")
      self.assertEqual(A.hey(35), "Boo")
      self.assertEqual(B.hey(42), "Woo")
      self.assertEqual(B.hey(35), "Bah")
