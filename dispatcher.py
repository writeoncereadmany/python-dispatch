class MethodDispatcher:

   def __init__(self, instance, dispatcher):
      self.instance = instance
      self.dispatcher = dispatcher

   def __call__(self, *args):
      return self.dispatcher(self.instance, *args)

class Dispatcher(object):

   def __init__(self, name):
      self.name = name
      self.targets = []

   def add_target(self, pattern, function):
      self.targets.append(Dispatchable(pattern, function))

   def add_default(self, function):
      self.default = function

   def __get__(self, instance, clazz):
      if(instance == None):
         return self
      return MethodDispatcher(instance, self)

   def __call__(self, *args):
      for function in self.targets:
         if function.matches(*args): return function(*args)
      if hasattr(self, 'default'):
         return self.default(*args)
      raise TypeError('{0}() is a case function which has no implementation which matches args {1}'.format(self.name, args))

class Dispatchable:

   def __init__(self, pattern, function):
      self.pattern = pattern
      self.function = function

   def matches(self, *args):
      return self.pattern.matches(*args)

   def __call__(self, *args):
      return self.function(*args)
