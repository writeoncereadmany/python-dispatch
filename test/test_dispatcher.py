import unittest
from dispatcher import Dispatcher
from pattern import Pattern

class DispatcherTest(unittest.TestCase):

   def test_empty_dispatcher_always_raises_TypeError(self):
      dispatcher = Dispatcher('func')
      self.assertRaises(TypeError, dispatcher, 5)

   def test_dispatches_correct_method(self):
      dispatcher = Dispatcher('func')
      dispatcher.add_target(Pattern(lambda num: num % 2 == 0), lambda x: 'even')
      dispatcher.add_target(Pattern(lambda num: num % 2 != 0), lambda x: 'odd')
      
      self.assertEqual(dispatcher(2), 'even')
      self.assertEqual(dispatcher(3), 'odd')

   def test_uses_default_if_no_match(self):
      dispatcher = Dispatcher('func')
      dispatcher.add_target(Pattern(5), lambda x: x*x)
      dispatcher.add_default(lambda x: x*2)

      self.assertEqual(dispatcher(5), 25)
      self.assertEqual(dispatcher(3), 6)
