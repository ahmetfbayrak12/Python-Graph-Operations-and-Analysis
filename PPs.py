#!/usr/bin/python
#  -*- coding: utf-8 -*-


import inspect, os

def create_commands(file):
    getfile = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + file, "r")
    mycommands = getfile.read()
    commandlist = mycommands.split(",")
    return commandlist

def find_cities(file):
    cities_file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + file, "r")
    cities_all = cities_file.read()
    cities = cities_all.splitlines()
    return cities

mydict = {}

cities = find_cities("paths.txt")

for line in cities:
    keyim = line.split(":")[0]
    valim = line.split(":")[1]
    mydict[keyim] = valim
keys = list()

for i, k in mydict.iteritems():
    keys.append(i)
    mylist = list()
    k = str(k)
    ks = k.split(" ")
    for t in ks:
        mylist.append(t)
    for r in mylist:
        if r in mydict.keys():
            val = mydict[r]
            val = str(val)
            vallist = val.split(" ")
            for w in vallist:
                mylist.append(w)
    for r in mylist:
         if r in mydict.keys():
            val = mydict[r]
            val = str(val)
            vallist = val.split(" ")
            for w in vallist:
                mylist.append(w)
    myset = set(mylist)
    print i, myset
commandlist = create_commands("commandsP2.txt")
for t in commandlist:
    if t not in keys:
        print "City '" + str(t) +"' has no reachable neighbour "

