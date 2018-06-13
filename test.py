from infixtotree import to_expr_tree
from evalpostfix import eval_postfix
from vartree import VarTree

def test(expr):
    tree = to_expr_tree(expr)
    print (expr, ':', tree.evaluate(V1))
    if '?' not in expr:
        print("from postfix:", eval_postfix(V2, tree.postfix())

V1 = VarTree()
V2 = VarTree()
test("a = 2 + 3*4")
test("b = a > 0 ? a+1 : a-1")
