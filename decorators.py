from inspect import currentframe
from pattern import Pattern
from dispatcher import Dispatcher

def case(*pattern):
   def decorator(func):
      dispatcher = get_dispatcher(func.__name__)
      dispatcher.add_target(Pattern(*pattern), func)
    
      return dispatcher

   return decorator

def default(func):
   dispatcher = get_dispatcher(func.__name__)
   dispatcher.add_default(func)

   return dispatcher

def _(arg): return True

def get_dispatcher(name):
   # get stack frame from which case/default is called, look to see if name exists in locals, 
   # if so use that, otherwise create a new one
   # one level back is case or default. one more level is wherever decorator is called from
   # note that this is shenanigans of the highest order, and anything which changes the call stack
   # will break this immediately.
   calling_frame_locals = currentframe().f_back.f_back.f_locals
   if name in calling_frame_locals:
      dispatcher = calling_frame_locals[name]
      if isinstance(dispatcher, Dispatcher):
         return dispatcher
      else:
         raise SyntaxError('{0} already defined, and is not a case function'.format(name))
   else:
      return Dispatcher(name)

