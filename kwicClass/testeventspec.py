import eventspec

es = eventspec.EventSpec("kwic.fsm")

es.event('callConstructor') 
es.event('callAddText')
es.event('regularBreaks')
es.event('breakingRegularly') 
es.event('splitWords')
es.event('finishedShift') 
es.event('callAddText')
es.event('regularBreaks')
es.event('runningText') 
es.event('callAddText')
es.event('regularBreaks')
es.event('runningText') 
es.event('callIndex') 
es.event('completeRunningIndex')
es.event('breakingRegularly')
es.event('splitWords') 
es.event('finishedShift') 
es.event('printingIndex') 
es.event('callListPairs') 
es.event('completeListPairs')
es.event('finishedCheckingPairs') 
es.event('printLP')


es.printLog()
