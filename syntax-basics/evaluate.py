from vartree import VarTree
from peekable import Peekable, peek
from newsplit import new_split_iter
from infixtotree import to_expr_tree, define_func
import math

def evaluate(expr):
    itera = Peekable(new_split_iter(expr))
    if peek(itera) == "deffn":
        name, p, body = define_func(itera)
        functions.assign(name, (p, body))
    else:
        print(expr,':',to_expr_tree(expr).evaluate(variables, functions))



functions = VarTree()
variables = VarTree()

