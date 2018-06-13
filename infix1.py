from peekable import Peekable, peek
from newsplit import new_split_iter

def eval_infix_sum(iterator):
    answer = eval_infix_product(iterator)
    while iterator.peek() == '+' or iterator.peek() == '-':
        opp = next(iterator)
        value = eval_infix_product(iterator)
        if opp == '+':
            answer = answer + value
        elif opp == '-':
            answer = answer - value
    return answer

def eval_infix_product(iterator):
    answer = eval_infix_factor(iterator)
    while iterator.peek() == '*' or iterator.peek() == '/' or iterator.peek() == '%':
        opp = next(iterator)
        value = eval_infix_factor(iterator)
        if opp == '*':
            answer = answer * value
        elif opp == '/':
            answer = answer/value
        elif opp == '%':
            ans = answer % value
    return answer

def eval_infix_factor(iterator):
    if (iterator.peek().isdigit()):
        return int(next(iterator))
    elif iterator.peek() == '(':
        next(iterator)
        ans = eval_infix_sum(iterator)
        next(iterator)
    return answer

def eval_infix_iter(iterator):
    return eval_infix_sum(Peekable(iterator))

def eval_infix(expr):
    return eval_infix_iter(new_split_iter(expr))

if __name__ == "__main__":
    print ( eval_infix_iter( iter(["2","+","3"])) )
    print ( eval_infix("15 ") )
    print ( eval_infix( " 2 * 3 + 1  " ) )
    print ( eval_infix( " 2 + 3 * 1" ) )



