from condition import Condition

class Pattern:

   def __init__(self, *conditions):
      self.conditions = [Condition(condition) for condition in conditions]

   def matches(self, *args):
      return (len(args) == len(self.conditions) 
              and all(condition.matches(arg) for (condition, arg) in zip(self.conditions, args)))
