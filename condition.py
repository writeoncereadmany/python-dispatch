from inspect import isclass, isfunction

class Condition:

   def __init__(self, condition):
      if isclass(condition):
         self.matcher = lambda instance: isinstance(instance, condition)
      elif isfunction(condition):
         self.matcher = condition 
      else:
         self.matcher = lambda instance: instance == condition

   def matches(self, argument):
      return self.matcher(argument)
