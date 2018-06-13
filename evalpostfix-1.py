from linkedlist import linkedlist
from vartree import VarTree
from infixtoiter import to_postfix 

def eval_postfix(Tree, iterator):
    operator = ['+', '-', '*', '/', '%', '=']
    stack = linkedlist()
    for token in iterator:
        if token in operator:
            if token == '=':
                right = stack.pop()
                left = stack.pop()
                if right.isalpha():
                    right = Tree.lookup(right)
                Tree.assign(left, right)
                stack.push(left)
            else:
                right = stack.pop()
                if right.isalpha():
                    right = Tree.lookup(right)
                left = stack.pop()
                if left.isalpha():
                    left = Tree.lookup(left)
                stack.push(str(eval(str(left) + token + str(right))))
        else:
            stack.push(token)

    returval = stack.pop()
    if returval.isalpha():
        return Tree.lookup(returval)
    return returval

if __name__ == '__main__':
    print(eval_postfix("b=8"))
    print(eval_postfix("b * 6"))
    print(eval_postfix('y = b + 7'))
    print(eval_postfix('b'))
