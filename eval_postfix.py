from vartree import VarTree
from linkedlist import linkedlist
from infixtopostfix import to_postfix

ops = ['+','-','/','%','*','=']
var = VarTree()

def eval_postfix(expr):
    stack = linkedlist(expr)
    for i in expr:
        if i in ops:
            if i == "=":
                second = stack.pop()
                first = stack.pop()
                if second.isalpha():
                    second = var.lookup(second)
                var.assign(first, second)
                stack.push(first)
            else:
                second = stack.pop()
                if second.isalpha():
                    second = var.lookup(second)
                first = stack.pop()
                if first.isalpha():
                    first = var.lookup(first)
                stack.push(str(eval(str(first) + i + str(second))))
        else:
            stack.push(i)
                
    value = stack.pop()
    if value.isalpha():
        return var.lookup(value)
    return value


vars = VarTree()
if __name__ == '__main__':
    print(eval_postfix(to_postfix("b * 3")))
    print(eval_postfix(to_postfix("b = 9")))
    print(eval_postfix(to_postfix("ba = 20")))
    print(eval_postfix(to_postfix("ba + 1")))
