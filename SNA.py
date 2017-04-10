

import inspect, os

def dosya_al(filename):
    opened_file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + filename, "r")
    readed_text = opened_file.read()
    readed_list = readed_text.splitlines()
    readed_dict = dict()
    for i in readed_list:
        nereden = i.split(":")[0]
        nereye = i.split(":")[1]
        readed_dict[nereden] = nereye
    return readed_dict

def dosya_al_commands(filename):
    opened_file = open(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/" + filename, "r")
    readed_text = opened_file.read()
    readed_list = readed_text.splitlines()
    return readed_list

def call_func(file):
    cmdlist = dosya_al_commands(file)
    for i in cmdlist:
        i = str(i)
        if i.split()[0] == "AU":
            try:
                parameter1 = i.split()[1]
                parameter2 = i.split()[2]
                AU(parameter1, parameter2)
            except:
                print "Wrong input type for 'AU'"

        elif  i.split()[0] == "RU":
            try:
                parameter1 = i.split()[1]
                RU(parameter1, parameter2)
            except:
                print "Wrong input type for 'RU'"

        elif  i.split()[0] == "AR":
            try:
                parameter1 = i.split()[1]
                parameter2 = i.split()[2]
                AR(parameter1, parameter2)
            except:
                print "Wrong input type for 'AR'"

        elif  i.split()[0] == "RR":
            try:
                parameter1 = i.split()[1]
                parameter2 = i.split()[2]
                RR(parameter1, parameter2)
            except:
                print "Wrong input type for 'RR'"

        elif  i.split()[0] == "PA":
            try:
                parameter1 = i.split()[1]
                PA(parameter1, parameter2)
            except:
                print "Wrong input type for 'PA'"

        elif  i.split()[0] == "SA":
            try:
                parameter1 = i.split()[1]
                parameter2 = i.split()[2]
                SA(parameter1, parameter2)
            except:
                print "Wrong input type for 'SA'"

def AU(a, b):
    print "AU executed"
def RU(a):
    print "RU executed"
def AR(a, b):
    print "AR executed"
def RR(a, b):
    print "RR executed"
def PA(a):
    print "PA executed"
def SA(a, b):
    print "SA executed"


call_func("commandsP1.txt")