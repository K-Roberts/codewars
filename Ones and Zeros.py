#Given an array of one's and zero's convert the equivalent binary value to an integer.



def binary_array_to_number(arr):
    base = 2
    binary_number = 0
    j=0
    for i in range(len(arr)-1, -1, -1):
        if arr[j] == 1:
            binary_number += base**i
        j+=1    
    return binary_number


Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11



#Below is the most popular answer on Codewars as of 11.11.18

def binary_array_to_number(arr):
    return int(''.join(str(a) for a in arr), 2)
