#!/usr/bin/python
import sys
import os

def est_price(a, t0, t1):
    return float(t0) + float(t1) * float(a) * 100000

def recup_teta():
    try:
        fo = open("tetadata.csv", "r+")
    except IOError:
        fo = open("tetadata.csv", "w+")
        fo.write("0,0")
        fo.close()
        fo = open("tetadata.csv", "r+")
    teta = fo.read()
    t = teta.split(',')
    fo.close()
    return t
#Debut
t = recup_teta();
a = raw_input("Entrer un kilometrage: ")
print est_price(a, t[0], t[1])
