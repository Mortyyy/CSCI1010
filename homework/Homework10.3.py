# -*- coding: utf-8 -*-
"""
@author: Alex

Takes the name of a friend as input and parses through the phonebook. 
If the name is in the phonebook, print the number of that friend otherwise print 'Not Found'.

"""

phonebook = {'sam': 999122222, 'tom': 111222222, 'harry':123333333}

def lookup(name):
    if name.lower() not in phonebook:
        print('Not Found.')
        return
    else:
        print(phonebook[name.lower()])

lookup('Tom')
lookup('Bill')
