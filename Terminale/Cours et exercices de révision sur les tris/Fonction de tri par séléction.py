# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 09:58:58 2022

@author: ccrouan
"""

def Selection(L):
    if len(L) == 1:
        return L
    else:
        m = min(L)
        L.remove(m)
        return [m]+Selection(L)
    
def indice_ins(lst, x):
    return (0 #if len(lst)==0 
        else len(lst) if x > lst[-1] 
    else indice_ins(lst[:-1], x)
    )
def tri(lst, i=1):
    ii = indice_ins(lst[:i], lst[i]) if i == len(lst) else 0
    return (lst if i==len(lst)
            else tri(lst[:ii] + [lst[i]] + lst[ii:i] + lst[i+1:], i+1)
            )
