from fastkwic import kwic as kwicFast
from testkwic import kwic as kwicTest
from kwic import kwic as kwic
import pprint
import sys
import time


x = open('myOutput.txt','w')
x.truncate()
start_time = time.time()
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
t = time.time() - start_time
print("--- %s seconds ---" % (t))

# fastT = []
# kwicT = []

# fn = sys.argv[1]


# with open(fn,'r') as f:
#     data = f.read()
# for i in xrange(1):
#     start = time.time()
#     kout = kwic(data,periodsToBreaks=True,listPairs=True)
#     kwicT.append(time.time()-start)

# for i in xrange(1):
#     start = time.time()
#     kout = kwicFast(data,periodsToBreaks=True,listPairs=True)
#     fastT.append(time.time()-start)


# f.close()

# print("FKWIC : "+ str(float((sum(fastT)) / max(len(fastT),6))))
# print("NKWIC : "+ str(float((sum(kwicT)) / max(len(kwicT),6))))
# print("FKWIC IS FASTER BY: "+ str(float((sum(kwicT)) / max(len(kwicT),6)-(sum(fastT)) / max(len(fastT),6))))