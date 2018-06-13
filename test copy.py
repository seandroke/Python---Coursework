from infixtotree import to_expr_tree
from evaluate import evaluate
from vartree import VarTree

def test(expr):
    tree = to_expr_tree(expr)
    print (expr, ':', tree.evaluate(V))
    if '?' not in expr:
        print("from postfix:", eval_postfix(tree.postfix()))

V = VarTree()
test("a = 2 + 3*4")
test("b = a > 0 ? a+1 : a-1")
