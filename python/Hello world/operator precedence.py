x = 10 + 3 * 2
print(x) # prints 16 because multiplication has higher precedence than addition

#parentheses have the highest precedence, so we can use them to change the order of operations
#order of operations priority: parentheses > exponentiation > multiplication/division > addition/subtraction
x = (10 + 3) * 2 + 1 - 3
print(x) # prints 27 because the operations are evaluated in the following order: parentheses, multiplication, addition, and subtraction