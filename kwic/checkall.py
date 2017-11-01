from kwic import *
import pprint

x = open('myOutput.txt','w')
x.truncate()
for l in open("tocheck.txt"):
    x.write("="*50)
    x.write('\n')
    input = l[:-1]
    x.write("INPUT: "+input)
    x.write('\n')
    v = eval("kwic("+input+")")
    x.write("OUTPUT:\n")
    pprint.pprint(v, x)
    x.write('\n')    