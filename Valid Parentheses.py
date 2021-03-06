'''
PROBLEM STATEMENT:
Write a function called that takes a 
string of parentheses, and determines 
if the order of the parentheses is valid. 
The function should return true if the 
string is valid, and false if it's invalid.

EXAMPLES:
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
'''


def valid_parentheses(string):
    left_count = 0
    right_count = 0
    for i in range(len(string)):
        if string[i] == '(':
            left_count+=1
        if string[i] == ')':
            right_count+=1
        if right_count > left_count:
            return False
    if left_count == right_count:
        return True
    else:
        return False
