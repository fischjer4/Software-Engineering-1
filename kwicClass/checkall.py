# from fastkwic import kwic as kwic
# import pprint
# import sys
# import time

# x = open('myOutput.txt','w')
# x.truncate()
# start_time = time.time()
# for l in open("tocheck.txt"):
#     x.write("="*50)
#     x.write('\n')
#     input = l[:-1]
#     x.write("INPUT: "+input)
#     x.write('\n')
#     v = eval("kwic("+input+")")
#     x.write("OUTPUT:\n")
#     pprint.pprint(v, x)
#     x.write('\n')
# t = time.time() - start_time
# print("--- %s seconds ---" % (t))


from kwic import Kwic
import pprint
import time

def kwic1(strng, ignoreWords=[], periodsToBreaks=False, listPairs = False):
    kw = Kwic(ignoreWords=ignoreWords, periodsToBreaks=periodsToBreaks)
    kw.addText(strng)
    if listPairs:
        return (kw.index(), kw.listPairs())
    else:
        return kw.index()

x = open('myOutput.txt','w')
x.truncate()
start_time = time.time()
for l in open("tocheck.txt"):
    x.write("="*50)
    x.write('\n')
    input = l[:-1]
    x.write("INPUT: "+input)
    x.write('\n')

    v = eval("kwic1("+input+")")
    x.write("OUTPUT:\n")
    pprint.pprint(v, x)
    x.write('\n')
t = time.time() - start_time
print("--- %s seconds ---" % (t))
