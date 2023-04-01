# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 09:47:28 2022

@author: ccrouan
"""

def tourniquet(p1,p2,p3):
    liste = []
    if len(p1) == 0 and len(p2) == 0 and len(p3) == 0:
        return []
    else:
        if len(p1) != 0:
            liste.append(p1[0])
        if len(p2) != 0:
            liste.append(p2[0])
        if len(p3) != 0:
            liste.append(p3[0])
        return liste + tourniquet(p1[1:], p2[1:], p3[1:])

def plus_court(proc_list):
    if len(proc_list) ==  1:
        return proc_list[0]
    i_min = 0
    for i in range(1, len(proc_list)):
        if len(proc_list[i])<len(proc_list[i_min]):
            i_min = i
    return proc_list[i_min]+plus_court(proc_list[:i_min]+proc_list[i_min+1:])

proc1=["i1","i2","i3","i4","i5","i6","i7"]
proc2=["ins1","ins2","ins3"]
proc3=["instru1","instru2","instru3","instru4","instru5"]

print(tourniquet(proc1,proc2,proc3))

print(plus_court([proc1,proc2,proc3]))