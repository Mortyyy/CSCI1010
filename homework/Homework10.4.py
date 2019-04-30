# -*- coding: utf-8 -*-
"""

@author: Alex

This is a program that removes these duplicate values from the student data. 
Your program must create a new dictionary OR update the existing one with no repeated records.

"""

#Given from assignment.
student_data = {
    'id1':{'name':['Sara'],'class':['V'],'subject_integration':['english, math, science']},
    'id2':{'name':['David'],'class':['V'],'subject_integration':['english, math, science']},
    'id3':{'name':['Sara'],'class':['V'],'subject_integration':['english, math, science']},
    'id4':{'name':['Surya'],'class':['V'],'subject_integration':['english, math, science']},
    'id5':{'name':['Dan'],'class':['V'],'subject_integration':['english, math, science']},
    'id6':{'name':['Dan'],'class':['V'],'subject_integration':['english, math, science']}
    }

shortlist = {}
for key, value in student_data.items():
    if value not in shortlist.values():
        shortlist[key] = value

print(shortlist)
