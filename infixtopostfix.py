from newsplit import new_split_iter
from peekable import Peekable, peek

def postfix_assign(expr):
    yield from postfix_sum(expr)
    while (peek(expr) == '='):
        token = next(expr)
        yield from postfix_assign(expr)
        yield token

def postfix_sum(expr):
    yield from postfix_product(expr)
    while (peek(expr) == '+') or (peek(expr) == '-'):
        token = next(expr)
        yield from postfix_product(expr)
        yield token

def postfix_product(expr):
    yield from postfix_factor(expr)
    while (peek(expr) == '*') or (peek(expr) == '/') or (peek(expr) == '%'):
        token = next(expr)
        yield from postfix_factor(expr)
        yield token

def postfix_factor(expr):
    if (peek(expr) == '('):
        next(expr)
        yield from postfix_assign(expr)
        next(expr)
    else:
        yield next(expr)

def to_postfix(expr):
    return postfix_assign(Peekable(new_split_iter(expr)))



