'''
Created on Nov 14, 2018

@author: kroberts

PROBLEM STATEMENT:

Your job is to write a function which increments a string, to create a new string. 
If the string already ends with a number, the number should be incremented by 1. If 
the string does not end with a number the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100
'''


def increment_string(strng):
    
    #If there is an empty string -----> output '1'
    if len(strng) == 0:
        return '1'
    
    
    #Searching for nearest non-digit(character) from end of string, if no characters are found in string, set index to -1
    for i in range(len(strng)-1, -1, -1):
        if not strng[i].isdigit():
            idx = i
            break
        else:
            idx = -1
    
    #If no digit is found at end of string ------> output (string + '1')
    if idx == len(strng) - 1:
        return strng + '1'
    
    #When character is found after incremented digits ------> output (string + str(number+1))
    else:
        ltr_stg = strng[:idx+1]
        number_stg = strng[idx+1:]
        len1 = len(number_stg)
        number = int(number_stg)
        number+=1
        new_number_stg = str(number)
        len2 = len(new_number_stg)
        if len2 >= len1:
            return ltr_stg + new_number_stg
        if len2 < len1:
            return ltr_stg + '0'*(len1-len2) + new_number_stg
              
        
    

print(increment_string('foo')) #--------------> 'foo1'
print(increment_string('')) #-----------------> '1'
print(increment_string('there009')) #---------> 'there010'
print(increment_string('foo9')) #-------------> 'foo10'
print(increment_string('hithere34')) #--------> 'hithere35'
