#!/usr/bin/python
from sys	import exit
import os

# from open_teta import est_price as est_price
# from open_teta import recup_teta as recup_teta


def changeteta(t):
    os.remove("tetadata.csv")
    fo = open("tetadata.csv", "w+")
    # r = teta.split(',')
    fo.write(str(t[0]) + "," + str(t[1]))
    fo.close()
#test check result
#    fo = open("tetadata.csv", "r+")
#    teta = fo.read()
#    print teta
def est_price(a, t0, t1):
    return (float(t0) + float(t1)) * float(a) * 100000

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

def creat_tab(value):
    tab = []
    for v in value:
        t = v.split(',')
        try:
            if t[0].isdigit() and t[1].isdigit():
               tab.append([float(t[0]) / 100000 , float(t[1]) / 100000 ])
        except StandardError:
            continue
    for v in tab:
        print v
    # print tab[3][1]
    return tab

def theta_finder(tab, t):
    tmp_theta0 = 1.0
    tmp_theta1 = 1.0
    sum_theta_0 = 0
    sum_theta_1 = 0
    learning_rate = 0.1
    while(abs(tmp_theta0) > 0.1 and abs(tmp_theta1) > 0.1):
        for i in range(len(tab)):
            sum_theta_0 += est_price(tab[i][0], t[0], t[1]) - tab[i][1]
            sum_theta_1 += (est_price(tab[i][0], t[0], t[1]) - tab[i][1]) * tab[i][0]
        tmp_theta0 = learning_rate * sum_theta_0 / len(tab)
        tmp_theta1 = learning_rate * sum_theta_1 / len(tab)
        t[0] = (float(t[0]) - tmp_theta0) / 50000
        t[1] = (float(t[0]) - tmp_theta1) / 50000
        # print t[0]
        # print t[1]
        # print "^^^^^^^^"
    return t

#debut
try:
    fo = open("data.csv", "r+")
except IOError:
    print "data.csv don't exist. please enter set for continue"
    exit(0)
value = fo.read()
value = value.split('\n')
fo.close()
tab = creat_tab(value);
t = recup_teta();
print "======="
print t
print "======="
tmp = theta_finder(tab, t);
changeteta(tmp);
