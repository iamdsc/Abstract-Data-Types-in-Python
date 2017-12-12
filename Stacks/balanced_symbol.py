from stack import Stack

# Complete balance checker for symbols : '[ { ( ) } ]'

def sym_checker (symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top=s.pop()
                if not matches(top, symbol):
                    balanced = False
        index=index+1
        
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches(op, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(op) == closes.index(close)

print(sym_checker('{{([][])}()}'))
print(sym_checker('[{()]'))




    
