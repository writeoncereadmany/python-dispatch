from inspect import isclass, isfunction
from duckface import Duckface

class Condition:

   def __init__(self, condition):
      if isclass(condition):
         self.matcher = lambda instance: isinstance(instance, condition)
      elif isinstance(condition, Duckface):
      	 self.matcher = lambda instance: condition.satisfied_by(instance)
      elif isfunction(condition):
         self.matcher = condition 
      else:
         self.matcher = lambda instance: instance == condition

   def matches(self, argument):
      return self.matcher(argument)
