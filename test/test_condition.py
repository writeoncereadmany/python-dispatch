import unittest
from condition import Condition

class ConditionTest(unittest.TestCase):

   def test_class_condition_satisfied_by_instances(self):

      class A: pass
      isAnA = Condition(A)
      anA = A()

      self.assertTrue(isAnA.matches(anA))

   def test_class_condition_satisfied_by_instances_of_subtypes(self):

      class A: pass
      class B(A): pass
      isAnA = Condition(A)
      aB = B()

      self.assertTrue(isAnA.matches(aB))

   def test_class_condition_not_satisfied_by_class_object(self):
   
      class A: pass
      isAnA = Condition(A)
      
      self.assertFalse(isAnA.matches(A))

   def test_class_condition_not_satisfied_by_instances_of_supertypes(self):

      class A: pass
      class B(A): pass
      isAB = Condition(B)
      anA = A()

      self.assertFalse(isAB.matches(A))

   def test_value_condition_satisfied_by_same_value(self):
 
      is5 = Condition(5)
      self.assertTrue(is5.matches(5))


   def test_value_condition_not_satisfied_by_other_value(self):

      is5 = Condition(5)
      self.assertFalse(is5.matches(7))


   def test_function_condition_satisfied_when_function_returns_true(self):

      isEven = Condition(lambda number: number % 2 == 0)
      self.assertTrue(isEven.matches(4))
      self.assertFalse(isEven.matches(3))

if __name__ == '__main__':
   unittest.main()
