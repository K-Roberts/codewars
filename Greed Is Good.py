'''
Created on Nov 13, 2018

@author: kroberts

PROBLEM STATEMENT:

Greed is a dice game played with five six-sided dice. Your mission, should you 
choose to accept it, is to score a throw according to these rules. You will always 
be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
 
A single die can only be counted once in each roll. For example, a "5" can only count 
as part of a triplet (contributing to the 500 points) or as a single 50 points, but not 
both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   50 + 2 * 100 = 250
 1 1 1 3 1   1000 + 100 = 1100
 2 4 4 5 4   400 + 50 = 450
'''

def score(dice):
    twos = dice.count(2)
    threes = dice.count(3)
    fours = dice.count(4)
    fives = dice.count(5)
    six = dice.count(6)
    ones = dice.count(1)
    total = 0
    if twos >= 3:
        total += 200
    if threes >= 3:
        total += 300
    if fours >= 3:
        total += 400
    if six >= 3:
        total += 600
    if fives >= 3:
        total += 500
        if fives > 3:
            total+=50*(fives-3)
    if ones >= 3:
        total += 1000
        if ones>3:
            total+=100*(ones-3)
    if fives < 3:
        total += 50*(fives)
    if ones < 3:
        total += 100*(ones)
    return total
