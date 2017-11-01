import sys
import subprocess

N = int(sys.argv[1])

for v in xrange(0,N):
    version = "kwic" + str(v) + ".py"
    for t in xrange(0,N):
        test = "testkwic" + str(t) + ".py"
        subprocess.call(["cp kwic.py oldkwic.py; cp " + version + " kwic.py"],shell=True)
        subprocess.call(["python " + test + " > & result.out"],shell=True)
        failed = False
        for l in open("result.out"):
            if "Traceback (most recent call last):" in l:
                failed = True
        if failed and (t <= v):
            print "TDD VIOLATION",version,"FAILS",test
        if not failed and (v < t):
            print "TDD VIOLATION",version,"PASSES",test            
