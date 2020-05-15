from peekable import Peekable, peek
from newsplit import new_split_iter
from exprtree import Var,Oper,Cond,Value,Functioncall

def tree_assign(iterator):
   a = tree_condition(iterator)
   if peek(iterator) == '=':
      operation = next(iterator)
      b = tree_assign(iterator)
      return Oper(a, operation, b)
   else:
      return a

def tree_condition(iterator):
   a = tree_relation(iterator)
   if peek(iterator) == "?":
      next(iterator)
      b = tree_assign(iterator)
      next(iterator)
      c = tree_assign(iterator)
      return Cond(a, b, c)
   else:
      return a

def tree_relation(iterator):
   a = tree_sum(iterator)
   if peek(iterator) == "<" or peek(iterator) == ">" or peek(iterator) == "<=" or peek(iterator) == ">=" or peek(iterator) == "==" or peek(iterator) == "!=":
      operation = next(iterator)
      b = tree_sum(iterator)
      return Oper(a, operation, b)
   else:
      return a

def tree_sum(iterator):
   a = tree_product(iterator)
   while peek(iterator) == '+' or peek(iterator) == '-':
      operation = next(iterator)
      b = tree_product(iterator)
      a = Oper(a, operation, b)
   return a

def define_func(iterator):
   next(iterator)
   name = next(iterator)
   next(iterator)
   parms = []
   while peek(iterator) is not ')':
      parms.append(next(iterator))
      if peek(iterator) == ',':
         next(iterator)
   next(iterator)
   next(iterator)
   body = tree_assign(iterator)
   return name, parms, body

def tree_factor(iterator):
   if peek(iterator) == '(':
      next(iterator)
      a = tree_assign(iterator)
      next(iterator)
      return a
   else:
      if peek(iterator)[0].isdigit():
         return Value(next(iterator))
      else:
         b = next(iterator)
         if peek(iterator) == "(":
            next(iterator)
            c = []
            while peek(iterator) != ")":
               a = tree_assign(iterator)
               c.append(a)
               if peek(iterator) == ",":
                  next(iterator)
            next(iterator)
            return Functioncall(b, c)
         else:
            return Var(b)

def tree_product(iterator):
   a = tree_factor(iterator)
   while peek(iterator) == '*' or peek(iterator) == '/' or peek(iterator) == '%':
      operation = next(iterator)
      b = tree_factor(iterator)
      a = Oper(a, operation, b)
   return a

def to_expr_tree(expr):
    return tree_assign(Peekable((new_split_iter(expr))))



