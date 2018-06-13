from peekable import Peekable, peek
from newsplit import new_split_iter
from exprtree import Var,Value,Oper,Cond
    
def postfix_conditional(iterator):
    t = postfix_keyword(iterator)
    if (peek(iterator) == "?"):
        next(iterator)
        true = postfix_keyword(iterator)
        if (peek(iterator)==":"):
            next(iterator)
            false = postfix_keyword(iterator)
            t = Cond(t,true,false)
    return t

def postfix_assign(iterator):
    left_child = postfix_conditional(iterator)
    if peek(iterator) == "=":
        next(iterator)
        right_child = postfix_assign(iterator)
        left_child = Oper(left_child,"=",right_child)
    return left_child

def postfix_relation(iterator):
    left_child = postfix_sum(iterator)
    while (peek(iterator) == "+=" or  peek(iterator) == "-=" or peek(iterator) == "*=" or peek(iterator) == "/=" or peek(iterator) == "==" or peek(iterator) == ">=" or peek(iterator) == "<=" or peek(iterator) == ">" or peek(iterator) == "<" or peek(iterator) == "!="):
        join = peek(iterator)
        next(iterator)
        right_child = postfix_sum(iterator)
        left_child = Oper(left_child,join,right_child)
    return left_child

def postfix_product(iterator):
    left_child = postfix_factor(iterator)
    while (peek(iterator) == "*" or peek(iterator)== "/" or peek(iterator) == "%" or peek(iterator) == "//"):
        join = peek(iterator)
        next(iterator)
        right_child = postfix_factor(iterator)
        left_child = Oper(left_child,join,right_child)
    return left_child

def postfix_keyword(iterator):
    left_child = postfix_relation(iterator)
    while (peek(iterator) == "and" or peek(iterator) == "or" or peek(iterator) == "not"):
        join = peek(iterator)
        next(iterator)
        right_child = postfix_relation(iterator)
        left_child = Oper(left_child,join,right_child)
    return left_child

def postfix_factor(iterator):
    if peek(iterator) == "(":                                  
            next(iterator)
            dub = postfix_assign(iterator)
            next(iterator)
            return dub
    else:
        if (peek(iterator).isdigit()):
            join = peek(iterator)
            next(iterator)
            return Value(join)
        elif (peek(iterator).isalpha()):
            join=peek(iterator)
            next(iterator)
            return Var(join)
            
def postfix_sum(iterator):
    left_child = postfix_product(iterator)
    while (peek(iterator) == "+" or peek(iterator) == "-"):
        join = peek(iterator)
        next(iterator)
        right_child = postfix_product(iterator)
        left_child = Oper(left_child,join,right_child)
    return left_child
                      
def to_expr_tree( expr ):    
    return postfix_assign(Peekable(new_split_iter(expr)))
