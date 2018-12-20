'''
PROBLEM STATEMENT:

Imagine that we have ATM with multiple currencies. The users can withdraw money of in any currency that the ATM has.

Our function must analyze the currency and value of what the users wants, and give money to the user starting from bigger values to smaller. The ATM gives the least amount of notes possible.

This kata has a preloaded dictionary of possible bank note values for different currencies (RUB, EUR, UAH, USD, CUP, SOS):

VALUES = { "EUR": [5, 10, 20, 50, 100, 200, 500], "USD": ... }
The function should return a string containing how many bank notes of each value the ATM will give out, for example:

"8 * 100 USD, 2 * 20 USD, 1 * 2 USD"
If it can't do that because there are no notes for this value, it should return:

"Can't do *value* *currency*. Value must be divisible by *amount*!"
(replace *value*, *currency* and *amount* with the relevant details)

If it doesn't have the requested currency at all, it should return:

"Sorry, have no *currency*."
Notes:
Letter case and word order doesn't matter in the input: e.g. "EUR 1000" and "1000eur" are the same. See test cases for more user input samples.
Do not create your own VALUES dictionary/hash or you'll get broken tests.
'''


import re
def atm(value):
    
    string = ''
    for key, val in VALUES.items():
        if key in value.upper():
           
            deposit = int(re.findall(r'[0-9]+', value)[0])
            
            if deposit%VALUES[key][0] == 0:
                for bill in VALUES[key][::-1]:
                    if deposit/bill > 1:
                        string += '%d * %d %s, ' % (int(deposit/bill), bill, key)
                        deposit = deposit%bill
                        if deposit == 0:
                            return string[:-2]
                    elif deposit%bill == 0:
                        string += '%d * %d %s, ' % (int(deposit/bill), bill, key)
                        return string[:-2]
            else:
                return 'Can\'t do %d %s. Value must be divisible by %d!' % (deposit, key, VALUES[key][0])
    else:
        return 'Sorry, have no %s.' % (re.findall(r'[a-zA-Z]+', value)[0].upper())
