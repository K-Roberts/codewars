'''
Created on Nov 13, 2018

@author: kroberts

PROBLEM STATEMENT:

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, 
pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names 
of people who like an item. It must return the display text as shown in the examples:

likes [] // must be "no one likes this"
likes ["Peter"] // must be "Peter likes this"
likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"

For 4 or more names, the number in and 2 others simply increases.
'''


def likes(names):
    num_people = len(names)
    if num_people > 0:
        if num_people == 1:
            print(names[0],'likes this')
        elif num_people == 2:
            print('%s and %s like this'%(names[0], names[1]))
        elif num_people == 3:
            print('%s, %s and %s like this'%(names[0],names[1],names[2]))
        else:
            print('%s, %s and %d others like this'%(names[0], names[1], num_people-2))
    else:
        print('no one likes this')    
